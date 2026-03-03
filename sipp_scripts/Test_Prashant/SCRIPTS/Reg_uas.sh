#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uas.xml 10.133.73.4 -i 10.133.39.159 -inf test420.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uas.xml 10.133.73.242 -i 10.133.39.159 -inf test_reg.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
/home/sipp/sipp.svn/sipp -sf ../XML/Register_Exp_Re-Reg_uas.xml 192.168.6.223 -i 192.168.6.5 -inf test_reg.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uas.xml 192.168.6.222 -i 192.168.6.5 -inf test420.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uas.xml 10.133.73.52 -i 10.133.39.159 -inf test420.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uas_retrans.xml 10.133.73.52 -i 10.133.39.159 -inf test420.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uas.xml 192.168.6.221 -i 192.168.6.5 -inf test420.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.146 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1 -m 1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.5.253 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
mv ../XML/Inbound_Basic_call_uas*.log ../SIPP_LOGS/
