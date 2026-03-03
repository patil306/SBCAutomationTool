/home/sipp/sipp.svn/sipp -sf ../XML/TC_NG_004_180SDP_PRACKSDP_UAC.xml 10.133.48.151:5060 -i 10.133.39.159 -inf test420.csv -p 5088 -t t1  -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/TC_NG_004_180SDP_PRACKSDP_UAC.xml 192.168.6.243:5060 -i 192.168.6.5 -inf test420.csv -p 5089 -t t1  -aa -trace_msg  -trace_err -m 1
mv ../XML/*.log ../SIPP_LOGS/
