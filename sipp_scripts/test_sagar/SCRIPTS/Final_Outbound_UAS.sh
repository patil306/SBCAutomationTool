/home/sipp/sipp.svn/sipp -sf ../XML/Final_Outbound_UAS.xml 10.133.73.51 -i 10.133.39.159 -inf testdemo.csv -p 5061 -t u1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Final_Outbound_UAS.xml 192.168.5.251 -i 192.168.5.12 -inf testdemo.csv -p 5071 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.146 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1 -m 1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.5.253 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
mv ../XML/Final_Outbound_UAS*messages.log ../SIPP_LOGS/
