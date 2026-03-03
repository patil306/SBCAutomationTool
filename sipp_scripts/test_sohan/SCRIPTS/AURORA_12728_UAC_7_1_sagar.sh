#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_12380_UAC.xml 10.133.48.157:5060 -i 10.133.39.159 -inf test420.csv -p 5075 -t t2  -aa -trace_msg  -trace_err -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_12728_UAC_issue_reproduce.xml 10.133.48.157:5060 -i 10.133.39.159 -inf test420.csv -p 5075 -t t1  -aa -trace_msg  -trace_err -m 1
/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_12728_UAC_issue_reproduce.xml 192.168.55.72::5060 -i 192.168.5.12 -inf test420.csv -p 5075 -t t1  -aa -trace_msg  -trace_err -m 1
mv ../XML/AURORA_12728_UAC*.log ../SIPP_LOGS/
