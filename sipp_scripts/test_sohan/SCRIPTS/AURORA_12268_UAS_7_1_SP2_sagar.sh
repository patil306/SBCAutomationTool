/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_12268_UAS_SUBSCRIBE_METHOD.xml 192.168.55.72:5060 -i 192.168.5.12 -inf testdemo.csv -p 5075 -t t1  -m 1 -aa -trace_msg  -trace_err -r 1
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14182_UAS_NOTIFY_METHOD.xml 192.168.6.245:5060 -i 192.168.6.5 -inf testdemo.csv -p 5097 -t t1  -m 1 -aa -trace_msg  -trace_err -r 100000
mv ../XML/AURORA_12268_UAS*.log ../SIPP_LOGS/
