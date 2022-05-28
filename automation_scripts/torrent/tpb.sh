#!/usr/bin/bash

if [ -z $1 ]; then 
	read -p "Please provide the search term: " query
else
	query=$1
fi

query=$(sed 's/ /%20/g' <<<$query)

info_hash=$(curl -s "https://piratebayorg.net/api.php?url=/q.php?q=${query}&cat=200" |
	jq -r '.[] | .info_hash + ", " + .size + ", [S:" + (.seeders|tostring) + " L:" + .leechers + "], " + .name' |
	numfmt -d ',' --field 2 --to=iec |
	fzf -d ',' --with-nth 2.. |
	cut -d ',' -f 1)

magnet="magnet:?xt=urn:btih:${info_hash}"

read -p "Do you want to download the file (y/n)? " ans

echo $magnet | xclip -sel c

if [[ $ans == 'y' ]]; then
	notify-send "Downloading file"
	aria2c -d "$HOME/Videos" "$magnet"
else
	echo "Magnet link copied to clipboard"
fi

