#!/bin/bash

pgrep FT || ./FT -f ft_420.cfg -c 1 -s 1000
while [ 1 ]
do
pgrep FT || ./FT -f ft_420.cfg -c 1 -s 1000

sleep 10s
done

