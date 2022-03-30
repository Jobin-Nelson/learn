#!/usr/bin/bash

if [ -z $1 ]; then
	read -p "Give me a file name: " file
fi

for file in $@; do
	if [ -f $file ]; then
		echo "It is a regular file"
	fi
done

ls -l 
