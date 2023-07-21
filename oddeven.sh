#!/bin/sh
clear
echo "enter any number"
read a
r=`expr $a % 2`
if [ $r == 0 ]
then
	echo "even"
else
	echo "odd"
fi
