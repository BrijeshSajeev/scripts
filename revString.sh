#!/bin/sh

clear

rev_str(){

rev=""
len=${#string}

for(( i=len-1; i>=0; i-- ))
do
	rev="$rev${string:$i:1}"
done
echo $rev
}

echo "enter any string"
read string
rev_str
