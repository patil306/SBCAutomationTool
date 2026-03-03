#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas_cancel.xml 192.168.6.242:5061 -i 192.168.6.5 -inf test420.csv -p 5076 -t l1 -r 10 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas_error.xml 192.168.6.242:5061 -i 192.168.6.5 -inf test420.csv -p 5076 -t l1 -r 10 -aa -trace_msg  -trace_err
/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.242:5061 -i 192.168.6.5 -inf test420.csv -p 5076 -t l1 -r 10 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.55.71:5060 -i 192.168.5.12 -inf test420.csv -p 5075 -t t1 -r 10 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.55.71:5061 -i 192.168.5.12 -inf test420.csv -p 5076 -t l1 -m 200 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.55.71:5060 -i 192.168.5.12 -inf test420.csv -p 5075 -t t1 -m 200 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.146 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1 -m 1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.5.253 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
mv ../XML/Basic_call_uas*.log ../SIPP_LOGS/
