/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_reinvite_call_uas_update.xml 192.168.55.79:5060 -i 192.168.5.12 -inf testdemo.csv -p 5089 -t t1  -m 200 -aa -trace_msg  -trace_err
mv ../XML/Basic_call_uas*.log ../SIPP_LOGS/
