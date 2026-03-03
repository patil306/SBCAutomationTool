#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_15765_UAC.xml 10.133.48.238:5060 -i 10.133.39.159 -inf test420.csv -p 5088 -aa -trace_msg  -trace_err -m 1
/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_15765_UAC_exceed_timer.xml 10.133.48.238:5060 -i 10.133.39.159 -inf test420.csv -p 5088 -aa -trace_msg  -trace_err -m 1
mv ../XML/AURORA_15765_UAC*.log ../SIPP_LOGS/
