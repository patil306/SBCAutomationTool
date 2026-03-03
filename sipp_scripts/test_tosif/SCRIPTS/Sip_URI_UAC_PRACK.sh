/home/sipp/sipp.svn/sipp -sf ../XML/Sip_URI_UAC_prack.xml 10.133.73.52:5060 -i 10.133.39.159 -inf test_prack.csv -p 5060 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Sip_URI_UAC_prack.xml 192.168.6.221:5060 -i 192.168.6.5 -inf test_prack.csv -p 5060 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Sip_URI_UAS.xml 192.168.6.221 -i 192.168.6.5 -inf test_prack.csv -p 5060 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.73.53:5060 -i 10.133.39.159 -inf testdemo.csv -p 5061 -t t1  -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.73.26:5060 -i 10.133.39.159 -inf testdemo.csv -p 5061 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml -r 1 -rp 20000 10.133.69.224 -i 10.133.39.159 -inf testdemo.csv -p 5060 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.69.224 -i 10.133.39.159 -inf testdemo.csv -p 5060 -t t1  -aa -trace_msg  -trace_err
#mv ../XML/Sip_URI_UAC_*.log ../SIPP_LOGS/
