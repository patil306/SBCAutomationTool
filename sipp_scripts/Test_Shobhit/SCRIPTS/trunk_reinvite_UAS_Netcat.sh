#!/bin/bash
/root/sipp.svn/sipp -sf ../XML/trunk_reinvite_UAS_New_Netcat.xml 10.133.36.209:5060 -i 10.133.36.8 -inf testdemo.csv -t t1 -m 100 -aa -trace_msg -trace_err
if [ -f s_data.txt ]
then
	grep "Hi This is Client" s_data.txt > /dev/null
	if [ $? == 0 ]; then
		echo  "Netcat server run suceesfully"
	else
		echo  "Necat server got failed"
	fi
fi

rm -rf s_data.txt
