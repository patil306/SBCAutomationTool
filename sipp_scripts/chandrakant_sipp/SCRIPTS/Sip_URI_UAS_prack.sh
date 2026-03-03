/home/sipp/sipp.svn/sipp -sf ../XML/Sip_URI_UAS_prack.xml 10.133.73.52 -i 10.133.39.159  -inf test_prack.csv -p 5060 -t t1  -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Sip_URI_UAS.xml 192.168.6.146 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Tel_URI_UAS.xml 192.168.5.253 -i 192.168.5.12 -inf testdemo.csv -p 5064 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.146 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1 -m 1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.5.253 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
mv ../XML/Basic_call_uas*.log ../SIPP_LOGS/
