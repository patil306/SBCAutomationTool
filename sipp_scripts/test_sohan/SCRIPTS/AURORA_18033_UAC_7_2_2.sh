#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_18033_UAC.xml 10.133.48.237:5060 -i 10.133.39.159 -inf test420.csv -p 5097 -aa -trace_msg  -trace_err -m 1
/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_18033_UAC_testcase2.xml 10.133.48.238:5060 -i 10.133.39.159 -inf test420.csv -p 5088 -aa -trace_msg  -trace_err -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_18033_UAC_reproduce.xml 10.133.48.237:5060 -i 10.133.39.159 -inf test420.csv -p 5097 -aa -trace_msg  -trace_err -m 1
mv ../XML/AURORA_18033_UAC_*.log ../SIPP_LOGS/
