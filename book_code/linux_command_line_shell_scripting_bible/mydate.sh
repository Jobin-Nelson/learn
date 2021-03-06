#!/usr/bin/bash
# calculate the number of days between two dates

date1="Jan 1, 2020"
date2="May 1, 2020"

time1=$(date -d "$date1" +%s)
time2=$(date -d "$date2" +%s)

dif=$[$time2 - $time1]
secondsInDay=$[24*60*60]
days=$[$dif / $secondsInDay]

echo "The difference between $date2 and $date1 is $days days"
echo "This is being run by $(basename $0) script"
exit
