#/home/sipp/sipp.svn/sipp -sf ../XML/Transfer_Target.xml 10.133.48.83:5060 -i 10.133.39.159 -inf testdemo.csv -p 5094 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Transfer_Target_14488.xml 192.168.55.78:5060 -i 192.168.5.12 -inf testdemo.csv -p 5095 -t t1 -aa -trace_msg  -trace_err -r 5
/home/sipp/sipp.svn/sipp -sf ../XML/Attended_Transfer_Target_Reinvite_11910.xml 10.133.48.238:5060 -i 10.133.39.159 -inf testdemo.csv -p 6027 -t t1 -aa -trace_msg  -trace_err -r 5
#/home/sipp/sipp.svn/sipp -sf ../XML/Transfer_Target_14488_722Setup.xml 192.168.6.244:5060 -i 192.168.6.5 -inf testdemo.csv -p 5098 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Transfer_Target_14488_722_DmitryCase.xml 192.168.6.244:5060 -i 192.168.6.5 -inf testdemo.csv -p 5098 -t t1 -aa -trace_msg  -trace_err

#/home/sipp/sipp.svn/sipp -sf ../XML/Transfer_Target_14488_722Setup.xml 192.168.6.244:5060 -i 192.168.6.5 -inf testdemo.csv -p 5094 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.146 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1 -m 1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.5.253 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
mv ../XML/Transfer_Target*messages.log ../SIPP_LOGS/
