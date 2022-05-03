#!/usr/bin/bash

if [ -z $1 ]; then 
	read -p "Please provide the search term: " query
else
	query=$1
fi

[ -z $2 ] && tries=3

res=$(curl -s "https://piratebayorg.net/api.php?url=/q.php?q=${query}&cat=200")
tracker="tr=udp%3A%2F%2F185.193.125.139%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A6969%2Fannounce&tr=udp%3A%2F%2Fmovies.zsw.ca%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.0x.tf%3A6969%2Fannounce&tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce&tr=udp%3A%2F%2F47.ip-51-68-199.eu%3A6969%2Fannounce"

if [ $tries -le $(echo $res | jq '.? | length') ]; then
	for (( i=0; i<tries; i++)); do
		name=$(echo  $res | jq -r ".[$i].name")
		size=$(echo  $res | jq -r ".[$i].size")
		date=$(echo  $res | jq -r ".[$i].added")
		encoded_name=$(echo -n $name | sed 's/\s/%20/g')
		info_hash=$(echo -n $res | jq -r ".[$i].info_hash")
		link="magnet:?xt=urn:btih:${info_hash}&dn=${encoded_name}&${tracker}"
		upload_date=$(date -d @"${date}" +%F)

		echo "Name: $name"
		echo -n "Size: "
		echo $size | awk '{ print $1/1024**3 "GB" }'
		echo "Upload date: $upload_date"
		echo -e "Link: ${link}\n\n"
	done
else
	echo "Not enough results for $tries tries"
fi
