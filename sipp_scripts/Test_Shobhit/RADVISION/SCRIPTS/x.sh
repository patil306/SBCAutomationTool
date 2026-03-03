#!/bin/bash
if [ -f c_data.txt ]
then
	grep Hi c_data.txt > /dev/null
	if [ $? == 0 ]; then
		echo "Netcat client run suceesfully"
	else
		echo "Necat Client fot failed"
	fi
fi
