#!/bin/sh
clear

echo "Enter Year >> "
read a
isleap=`expr $a % 4`
if [ $isleap == 0 ]
then
	echo "$a is the leap year"
else
	echo "$a is not a leap year"
fi
