#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uas.xml 192.168.5.35 -i 192.168.5.12 -inf test420.csv -p 55566 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_reinvite_call_uas.xml 192.168.5.35 -i 192.168.5.12 -inf test420.csv -p 55566 -t t1 -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_reinvite_call_uas_lmo.xml 192.168.45.143 -i 192.168.5.12 -inf test420.csv -p 5078 -t t1 -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uas.xml 192.168.5.143 -i 192.168.5.12 -inf test420.csv -p 5078 -t t1 -m 1
/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 192.168.45.143 -i 192.168.5.12 -inf test420.csv -p 5078 -t t1 -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 192.168.45.145 -i 192.168.5.12 -inf test420.csv -p 5077 -t t1 -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uas.xml 192.168.5.145 -i 192.168.5.12 -inf test420.csv -p 5077 -t t1 -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 192.168.5.143 -i 192.168.5.12 -inf test420.csv -p 5078 -t t1 -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.146 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1 -m 1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.5.253 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#mv ../XML/Basic_call_uas*.log ../SIPP_LOGS/
