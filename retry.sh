#!/bin/bash

n=0
command=$1

while [ $n -le 5 ] && ! $command; do
sleep $n
((n=n+1))
echo "Retry #$n"
done
