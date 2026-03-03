/home/sipp/sipp.svn/sipp -sf ../XML/multiUPD_uas-Re-INV-UAS.xml 192.168.6.244:5060 -i 192.168.6.5 -inf inf.csv -p 5072 -t t1  -m 1 -trace_msg  -trace_err
#/root/mahi/sipp-3.4.1/sipp-3.4.1/sipp -sf ../XML/multiUPD_uas-Re-INV-UAS.xml 192.168.5.110:5061 -i 192.168.5.36 -inf inf.csv -p 5061 -t l1  -m 1 -aa -trace_msg  -trace_err
mv ../XML/AURORA_13315_UAS*.log ../SIPP_LOGS/
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_12485_UAS.xml 192.168.6.246:5060 -i 192.168.6.5 -inf test420.csv -p 5060 -t t1  -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.146 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1 -m 1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.5.253 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
