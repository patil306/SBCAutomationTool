/home/sipp/sipp.svn/sipp -sf ../XML/Basic_Register_uac.xml 10.133.73.19:5061 -i 10.133.39.159 -inf num.csv -p 5061 -t l1 -max_socket 50000  -skip_rlimit -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_Register_uac.xml 10.133.73.26 -i 10.133.39.159 -inf test1.csv -t t1 -max_socket 5000 -skip_rlimit  false  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml -r 1 -rp 20000 10.133.69.224 -i 10.133.39.159 -inf testdemo.csv -p 5060 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.69.224 -i 10.133.39.159 -inf testdemo.csv -p 5060 -t t1  -aa -trace_msg  -trace_err
mv ../XML/Basic_Register_uac*.log ../SIPP_LOGS/
