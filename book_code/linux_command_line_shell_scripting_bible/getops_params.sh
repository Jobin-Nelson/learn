#!/usr/bin/bash
echo
while getopts :ab:c opt; do
	case "$opt" in
		a) echo "Found the -a option";;
		b) echo "Found the -b option with parameter value $OPTARG";;
		c) echo "Found the -c option";;
		*) echo "Unkown option: $opt at $[ $OPTIND - 1 ]";;
	esac
done
exit

