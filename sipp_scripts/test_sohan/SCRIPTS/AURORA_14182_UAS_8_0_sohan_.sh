#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14182_UAS.xml 192.168.6.245:5060 -i 192.168.6.5 -inf testdemo.csv -p 5097 -t t1  -m 1 -aa -trace_msg  -trace_err -r 100000
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14182_UAS_OPTIONS_INDIALOG.xml 192.168.6.245:5060 -i 192.168.6.5 -inf testdemo.csv -p 5097 -t t1  -m 1 -aa -trace_msg  -trace_err -r 100000
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14182_UAS_PRACK_METHOD.xml 192.168.6.245:5060 -i 192.168.6.5 -inf testdemo.csv -p 5097 -t t1  -m 1 -aa -trace_msg  -trace_err -r 100000
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14182_UAS_CANCEL_METHOD.xml 192.168.6.245:5060 -i 192.168.6.5 -inf testdemo.csv -p 5097 -t t1  -m 1 -aa -trace_msg  -trace_err -r 100000
/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14182_UAS_INVITE_METHOD.xml 192.168.6.245:5060 -i 192.168.6.5 -inf testdemo.csv -p 5097 -t t1  -m 1 -aa -trace_msg  -trace_err -r 100000
#/home/sipp/sipp.svn/sipp -sf ../XML/./AURORA_14182_UAS_ACK_METHOD.xml 192.168.6.245:5060 -i 192.168.6.5 -inf testdemo.csv -p 5097 -t t1  -m 1 -aa -trace_msg  -trace_err -r 100000
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14182_UAS_BYE_METHOD.xml 192.168.6.245:5060 -i 192.168.6.5 -inf testdemo.csv -p 5097 -t t1  -m 1 -aa -trace_msg  -trace_err -r 100000
#/home/sipp/sipp.svn/sipp -sf ../XML/Transferer.xml 192.168.6.245:5060 -i 192.168.6.5 -inf testdemo.csv -p 5097 -t t1  -m 1 -aa -trace_msg  -trace_err -r 100000
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14182_UAS_SUBSCRIBE_METHOD.xml 192.168.6.245:5060 -i 192.168.6.5 -inf testdemo.csv -p 5097 -t t1  -m 1 -aa -trace_msg  -trace_err -r 1
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14182_UAS_NOTIFY_METHOD.xml 192.168.6.245:5060 -i 192.168.6.5 -inf testdemo.csv -p 5097 -t t1  -m 1 -aa -trace_msg  -trace_err -r 100000
mv ../XML/AURORA_14182_UAS*.log ../SIPP_LOGS/
