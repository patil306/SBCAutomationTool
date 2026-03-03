/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_12268_UAC_SUBSCRIBE_METHOD.xml 10.133.48.87:5060 -i 10.133.39.159 -inf test420.csv -p 5097 -t t2  -aa -trace_msg  -trace_err -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14182_UAC_NOTIFY_METHOD.xml 10.133.48.87:5060 -i 10.133.39.159 -inf test420.csv -p 5097 -t t2  -aa -trace_msg  -trace_err -m 1
mv ../XML/AURORA_12268_UAC*.log ../SIPP_LOGS/
