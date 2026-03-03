#!/bin/bash
/home/sipp/sipp.svn/sipp -sf trunk_reinvite_UAC_Netcat.xml 192.168.5.30:5060 -i 192.168.5.12 -inf testdemo.csv -t t1 -m 1 -aa -trace_msg  -trace_err
if [ -f c_data.txt ]
then
	grep "Hi This is server" c_data.txt > /dev/null
	if [ $? == 0 ]; then
		echo  "Netcat client run suceesfully"
	else
		echo "Necat Client got failed"
	fi
fi
rm -rf c_data.txt
rm -rf *.log
