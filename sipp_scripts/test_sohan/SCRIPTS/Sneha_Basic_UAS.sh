#/home/sipp/sipp.svn/sipp -sf uas.xml 192.168.55.78:5060 -i 192.168.5.12 -inf test420.csv -p 5092 -t t1  -aa -trace_msg  -trace_err

#/home/sipp/sipp.svn/sipp -sf uas_srtp.xml 192.168.55.78:5060 -i 192.168.5.12 -inf test50001.csv -p 6005 -t t1  -aa -trace_msg  -trace_err

#/home/sipp/sipp.svn/sipp -sf uas_srtp.xml 192.168.55.78:5060 -i 192.168.5.12 -inf test50001.csv -p 6008 -t l1  -aa -trace_msg  -trace_err 
/home/sipp/sipp.svn/sipp -sf /home/sipp/test_Sneha/SCRIPTS/uas_srtp.xml 192.168.55.79:5061 -i 192.168.5.12 -inf /home/sipp/test_Sneha/SCRIPTS/test50001.csv -p 6029 -t l1  -m 1 -aa -trace_msg  -trace_err
