#/home/sipp/sipp.svn/sipp -sf ../XML/uac_XeroxCore_replaces.xml 10.133.48.155:5060 -i 10.133.39.159 -inf test40006.csv -p 6023 -aa -trace_msg  -t t1 -trace_err -m 1

/home/sipp/sipp.svn/sipp -sf ../XML/uac_XeroxCore_replaces.xml 192.168.55.76:5060 -i 192.168.5.12 -inf test50001.csv -p 5094 -aa -trace_msg  -t u1 -trace_err -m 1

#/home/sipp/sipp.svn/sipp -sf uac.xml 10.133.48.83:5060 -i 10.133.39.159 -inf test40006.csv -p 5094 -t t1 -aa -trace_msg  -trace_err -m 1

#/home/sipp/sipp.svn/sipp -sf uac_srtp.xml 10.133.48.168:5060 -i 10.133.39.159 -inf test50002.csv -p 6006 -t t1 -aa -trace_msg  -trace_err -m 1

#/home/sipp/sipp.svn/sipp -sf uac.xml 10.133.48.168:5060 -i 10.133.39.159 -inf test50001.csv -p 6004 -t t1 -aa -trace_msg  -trace_err -m 1

#/home/sipp/sipp.svn/sipp -sf uac_srtp.xml 10.133.48.238:5061 -i 10.133.39.159 -inf test50002.csv -p 6029 -t l1  -aa -trace_msg  -trace_err -m 1


