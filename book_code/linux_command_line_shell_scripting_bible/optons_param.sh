#!/usr/bin/bash
echo
while [ -n "$1" ]; do
	case $1 in
		-a) echo "found the -a option";;
		-b) echo "found the -b option";;
		--) shift
			break;;
		*) echo "$1 is not an option";;
	esac
	shift
done

echo 
count=0
for param in $@; do
	count=$[ $count + 1 ]
	echo "Parameter #$count: $param"
done
echo 
exit 0
