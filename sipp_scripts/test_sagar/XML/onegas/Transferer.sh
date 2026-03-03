#/home/sipp/sipp.svn/sipp -sf ../Transferer_error.xml 10.133.48.148:5060 -i 10.133.39.159 -inf testdemo.csv -p 5075  -aa -trace_msg  -trace_err -m 1 -t t1
/home/sipp/sipp.svn/sipp -sf ../Transferer.xml 10.133.48.149:5060 -i 10.133.39.159 -inf testdemo.csv -p 5075  -aa -trace_msg  -trace_err -m 1 -t t1
#/home/sipp/sipp.svn/sipp -sf ../Transferer.xml 10.133.48.157:5060 -i 10.133.39.159 -inf testdemo.csv -p 5075  -aa -trace_msg  -trace_err -m 1 -t t1
#/home/sipp/sipp.svn/sipp -sf transferer_mod5.xml 10.133.148.235 -i 10.133.39.159 -inf testdemo.csv -p 5075 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf transferer_mod2.xml 192.168.9.115 -i 192.168.5.12 -inf testdemo.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf transferer_mod2.xml 192.168.9.63 -i 192.168.5.12 -inf testdemo.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.146 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1 -m 1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.5.253 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
mv transferer_*messages.log ../../SIPP_LOGS/
mv transferer_*errors.log ../../SIPP_LOGS/
