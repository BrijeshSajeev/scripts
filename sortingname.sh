#!/bin/sh
clear
echo "Enter no of names >> "
read n

echo "Enter the names :)"

if test -f "sample"
then 
rm "sample"
fi

while test $n -gt 0
do
read s
echo $s | cat>>sample
n=`expr $n - 1`
done
echo "The sorted names >> "
sort "sample"
