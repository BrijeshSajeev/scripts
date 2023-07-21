#!/bin/sh
clear

echo "Enter no of emp >> "
read n

for (( i=0; i<n; i++ ))
do
ovt=0
tcost=0
echo "twt >>"
read twt
echo "act>>"
read at
echo "cost >>"
read cost

if [ $twt -gt $at ]
then
ovt=`expr $twt - $at`
tcost=`expr $ovt \* $cost`
echo "The overTime of emp > $i is $ovt"
echo "The Total cost of emp > $i is $tcost"
fi
done

