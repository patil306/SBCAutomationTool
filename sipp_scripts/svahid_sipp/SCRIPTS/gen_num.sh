#!/bin/bash

echo "SEQUENTIAL" >> reliance.csv

for ((a = 81002001, b = 81001001 ; a <= 81003000, b <= 81002000 ; a++, b++))
do
   echo "$a;$b;172.16.2.35;192.168.5.36;" >> reliance.csv
done
