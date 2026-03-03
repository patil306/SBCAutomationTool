#! /bin/bash


call_count=2*$1
media_ip=$2 
media_port=443

for((i=1;i<=$call_count;i=i+2))
do

   /home/sipp/chandrakant_sipp/SSL_CLIENTS/cert/SSLMirror -av $media_ip $media_port $media_port $i

done

exit
