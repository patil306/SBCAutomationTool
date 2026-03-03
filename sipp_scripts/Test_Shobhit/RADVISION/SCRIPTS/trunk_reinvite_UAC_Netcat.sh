#!/bin/bash
/root/sipp.svn/sipp -sf ../XML/trunk_reinvite_UAC_Netcat.xml 10.133.36.209:5060 -i 10.133.36.8 -inf testdemo.csv -t t1 -m 100 -aa -trace_msg  -trace_err
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
