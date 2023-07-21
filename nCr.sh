#!/bin/sh
clear

nCr(){
numerator=1
denominator=1

for (( i=1; i<=n; i++ ))
do
	numerator=`expr $numerator \* $i`
done

for (( j=1; j<=r; j++ ))
do
	denominator=`expr $denominator \* $j`
done
y=1
x=`expr $n - $r`
for (( k=1; k<=x; k++ ))
do
	y=`expr $y \* $k`
done

z=`expr $denominator \* $y`
res=`expr $numerator / $z`
echo "nCr of $n C $r is $res"

}

echo "enter n"
read n
echo "enter r"
read r
nCr
