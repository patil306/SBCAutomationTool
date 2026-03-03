#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14182_UAC.xml 10.133.48.238:5060 -i 10.133.39.159 -inf test420.csv -p 5088 -t t2  -aa -trace_msg  -trace_err -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14182_UAC_PRACK_METHOD.xml 10.133.48.238:5060 -i 10.133.39.159 -inf test420.csv -p 5088 -t t2  -aa -trace_msg  -trace_err -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14182_UAC_CANCEL_METHOD.xml 10.133.48.238:5060 -i 10.133.39.159 -inf test420.csv -p 5088 -t t2  -aa -trace_msg  -trace_err -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14182_UAC_INVITE_METHOD.xml 10.133.48.238:5060 -i 10.133.39.159 -inf test420.csv -p 5088 -t t2  -aa -trace_msg  -trace_err -m 1
/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14182_UAC_OPTIONS_INDIALOG.xml 10.133.48.238:5060 -i 10.133.39.159 -inf test420.csv -p 5088 -t t2  -aa -trace_msg  -trace_err -m 1
mv ../XML/AURORA_14182_UAC*.log ../SIPP_LOGS/
