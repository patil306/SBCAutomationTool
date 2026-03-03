#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uac.xml 10.133.39.186 -i 10.133.39.159 -inf test420.csv -p 5075 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uac_reinvite.xml 192.168.5.141 -i 192.168.5.12 -inf test420.csv -p 5075 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uac.xml 10.133.36.34 -i 10.133.39.159 -inf test420.csv -p 5075 -t u1 -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/Trunk_UAC_mod8.xml 10.133.36.34 -i 10.133.39.159 -inf test420.csv -p 5075 -t u1 -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_reinvite_call_uac.xml 10.133.36.34 -i 10.133.39.159 -inf test420.csv -p 5075 -t u1 -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.36.34 -i 10.133.39.159 -inf test420.csv -p 5075 -t u1 -m 1
/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uas.xml 10.133.36.34 -i 10.133.39.159 -inf test420.csv -p 5075 -t l1 -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uas.xml 10.133.36.36 -i 10.133.39.159 -inf test420.csv -p 5071 -t u1 -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.36.36 -i 10.133.39.159 -inf test420.csv -p 5071 -t t1 -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/options_uas_test1.xml 10.133.36.34 -i 10.133.39.159 -inf test420.csv -p 5075 -t u1 -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 10.133.39.159 -inf testdemo.csv -p 5061 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.73.53:5060 -i 10.133.39.159 -inf testdemo.csv -p 5061 -t t1  -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.73.26:5060 -i 10.133.39.159 -inf testdemo.csv -p 5061 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml -r 1 -rp 20000 10.133.69.224 -i 10.133.39.159 -inf testdemo.csv -p 5060 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.69.224 -i 10.133.39.159 -inf testdemo.csv -p 5060 -t t1  -aa -trace_msg  -trace_err
#mv ../XML/Basic_call_uac*.log ../SIPP_LOGS/
