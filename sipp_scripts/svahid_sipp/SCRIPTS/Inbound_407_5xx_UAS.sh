/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_407_5xx_Latest.xml 192.168.6.148 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.146 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1 -m 1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.5.253 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
mv ../XML/Inbound_407_5xx_uas*.log ../SIPP_LOGS/
