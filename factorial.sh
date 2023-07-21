#!/bin/sh
clear

fact(){
f=1

for((i=1; i<=a; i++))
do
	f=$(( $f * $i ))
done

echo $f
}
echo " Enter any Number >> "
read a
fact 





