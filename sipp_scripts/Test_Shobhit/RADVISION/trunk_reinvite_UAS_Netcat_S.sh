#!/bin/bash
/root/sipp.svn/sipp -sf ../XML/trunk_reinvite_UAS_New_Netcat_S.xml 10.133.36.209:5060 -i 10.133.36.8 -inf testdemo.csv -t t1 -m 1 -aa -trace_msg -trace_err
if [ -f s_data.txt ]
then
	grep "Hi This is Client" s_data.txt > /dev/null
	if [ $? == 0 ]; then
		echo -e "Netcat server run suceesfully"
	else
		echo "Necat server got failed"
	fi
else 
	echo "s_data.txt file is not present....Issue with the xml"
fi
rm s_data.txt

