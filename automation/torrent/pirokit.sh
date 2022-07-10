#!/usr/bin/bash

# get the top n movies links
query=$1
[ -z $query ] && read -p 'Enter a search term: ' query

baseUrl="https://www.1337xx.to"
cacheDir="$HOME/.cache/pirokit"
query=$(sed 's/ /+/g' <<<$query)

mkdir -p $cacheDir

curl -s "https://www.1337xx.to/search/$query/1/" > $cacheDir/tmp.html

# titles
grep -o '<a href="/torrent.*</a>' $cacheDir/tmp.html | sed 's/<[^>]*>//g' > $cacheDir/titles.txt

result_count=$(wc -l $cacheDir/titles.txt | awk '{print $1}')
if [ $result_count -lt 1 ]; then
	notify-send "😔 No result found. Try again"
	exit 0
fi

# seeders & leechers
grep -o '<td class="coll-2 seeds.*</td>\|<td class="coll-3 leeches.*</td>' $cacheDir/tmp.html |
	sed 's/<[^>]*>//g' | sed 'N;s/\n/ /' > $cacheDir/seedleech.txt

# size
grep -o '<td class="coll-4 size.*</td>' $cacheDir/tmp.html |
	sed 's/<span class="seeds">.*<\/span>//g' |
	sed 's/<[^>]*>//g' > $cacheDir/sizes.txt

# links
grep '/torrent/' $cacheDir/tmp.html |
	sed -E 's#.*(/torrent/.*)/">.*/#\1#' |
	sed 's/td>//g' > $cacheDir/links.txt

# cleaning up some data to display
sed 's/\./ /g; s/\-/ /g' $cacheDir/titles.txt |
	sed 's/[^A-Za-z0-9 ]//g' | tr -s " " > $cacheDir/tmp && mv $cacheDir/tmp $cacheDir/titles.txt

awk '{print NR " - ["$0"]"}' $cacheDir/sizes.txt > $cacheDir/tmp && mv $cacheDir/tmp $cacheDir/size.txt
awk '{print "[S: "$1 ", L: "$2"]" }' $cacheDir/seedleech.txt > $cacheDir/tmp && mv $cacheDir/tmp $cacheDir/seedleech.txt

# getting the line number
LINE=$(paste -d\   $cacheDir/sizes.txt $cacheDir/seedleech.txt $cacheDir/titles.txt |
	nl |
	fzf |
	cut -f1 |
	awk '{$1=$1; print}')

url=$(head -n $LINE $cacheDir/links.txt | tail -n +$LINE)
fullUrl="${baseUrl}${url}/"

# magnet link
curl -s $fullUrl > $cacheDir/tmp.html
magnet=$(grep -Po 'magnet:\?xt=urn:btih:[a-zA-Z0-9]*' $cacheDir/tmp.html | head -n 1)

if [ -z $magnet ]; then
	notify-send "Not able to get magnet link. Try again"
	exit 0
fi

echo $magnet | xclip -sel c

read -p 'Do you wish to download it (y/n)? ' ans
if [[ $ans -eq 'y' ]];then
	notify-send "Downloading file"
	aria2c -d $HOME/Videos --seed-time=0 $magnet
else
	echo 'magnet link copied to clipboard'
fi

