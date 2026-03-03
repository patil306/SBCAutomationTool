/home/sipp/sipp.svn/sipp -sf ../XML/uas_XeroxCore_200OK.xml 192.168.55.71:5060 -i 192.168.5.12 -inf test40006.csv -p 6021 -t u1  -aa -trace_msg  -trace_err

#/home/sipp/sipp.svn/sipp -sf uas_srtp.xml 192.168.55.78:5060 -i 192.168.5.12 -inf test50001.csv -p 6005 -t t1  -aa -trace_msg  -trace_err

#/home/sipp/sipp.svn/sipp -sf uas_srtp.xml 192.168.55.78:5060 -i 192.168.5.12 -inf test50001.csv -p 6008 -t l1  -aa -trace_msg  -trace_err 
#/home/sipp/sipp.svn/sipp -sf uas_forking.xml 192.168.55.80:5061 -i 192.168.5.12 -inf test50001.csv -p 6020 -t t1  -m 1 -aa -trace_msg  -trace_err
