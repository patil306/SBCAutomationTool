#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.245:5060 -i 192.168.6.5 -inf testdemo.csv -p 5088 -t t1  -m 200 -aa -trace_msg  -trace_err
/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas_sneha.xml 192.168.55.79:5060 -i 192.168.5.12 -inf testdemo.csv -p 5088  -m 200 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas_sneha.xml 192.168.55.79:5060 -i 192.168.5.12 -inf testdemo.csv -p 5088 -m 200 -aa -trace_msg  -trace_err
mv ../XML/Basic_call_uas*.log ../SIPP_LOGS/
