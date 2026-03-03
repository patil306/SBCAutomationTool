#!/bin/bash

n=0
while [ "$n" -lt 200 ] ; do
    date >> substats.txt
    echo "$n" >> substats.txt
    /home/sipp/test_Sahil/rajborelli-sipp/server/sbc191/SubscribeNoWait.sh &
    sleep 2
    /home/sipp/test_Sahil/rajborelli-sipp/client/sbc191/uacSubscribeNoWait.sh &
    n=$(( n + 1 ))
    sleep 20
done
