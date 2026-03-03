#/home/sipp/sipp.svn/sipp -sf ../XML/Transfer_Target.xml 192.168.6.222 -i 192.168.6.5 -inf testdemo.csv -p 5075 -t t1 -aa -trace_msg  -trace_err
/home/sipp/sipp.svn/sipp -sf Transfer_Target_mod1.xml 192.168.6.223 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Transfer_Target.xml 10.133.73.4 -i 10.133.139.159 -inf testdemo.csv -p 5071 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf Transfer_Target_mod1.xml 192.168.9.115 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.146 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1 -m 1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.5.253 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
mv ../XML/Transfer_Target*messages.log ../SIPP_LOGS/
