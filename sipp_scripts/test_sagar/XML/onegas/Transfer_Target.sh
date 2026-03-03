#/home/sipp/sipp.svn/sipp -sf ../Transfer_Target_error.xml 10.133.48.235:5060 -i 10.133.39.159 -inf testdemo.csv -p 5076  -aa -trace_msg  -trace_err -m 1 -t t1
/home/sipp/sipp.svn/sipp -sf ../Transfer_Target.xml 10.133.48.149:5060 -i 10.133.39.159 -inf testdemo.csv -p 5076  -aa -trace_msg  -trace_err -m 1 -t t1
#/home/sipp/sipp.svn/sipp -sf ../Transfer_Target.xml 10.133.48.157:5060 -i 10.133.39.159 -inf testdemo.csv -p 5076  -aa -trace_msg  -trace_err -m 1 -t t1
#/home/sipp/sipp.svn/sipp -sf Transfer_Target_mod1.xml 192.168.6.223 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Transfer_Target.xml 10.133.73.4 -i 10.133.39.159 -inf testdemo.csv -p 5071 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf Transfer_Target_BYEPhani.xml 10.133.73.4 -i 10.133.39.159 -inf testdemo.csv -p 5090 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf Transfer_Target_mod8.xml 10.133.73.4 -i 10.133.39.159 -inf testdemo.csv -p 5090 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf Transfer_Target_mod1.xml 192.168.9.115 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.146 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1 -m 1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.5.253 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
mv Transfer_Target*messages.log ../../SIPP_LOGS/
mv Transfer_Target*errors.log ../../SIPP_LOGS/
