#/home/sipp/sipp.svn/sipp -sf ../XML/Transferer.xml 10.133.73.48 -i 10.133.39.159 -inf testdemo.csv -p 5062 -t t1 -aa -trace_msg  -trace_err
/home/sipp/sipp.svn/sipp -sf Transferer_p_charge.xml 192.168.6.156 -i 192.168.6.5 -inf testdemo.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf transferer_mod2.xml 10.133.73.4 -i 10.133.39.159 -inf testdemo.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf transferer_mod2.xml 192.168.9.115 -i 192.168.5.12 -inf testdemo.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.146 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1 -m 1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.5.253 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
mv Transferer*messages.log ../SIPP_LOGS/
