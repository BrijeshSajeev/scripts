#!/bin/sh


b=0
until [ ! $b -lt 10 ]
do
  	echo "hi $b"
	b=`expr $b + 1`
done
