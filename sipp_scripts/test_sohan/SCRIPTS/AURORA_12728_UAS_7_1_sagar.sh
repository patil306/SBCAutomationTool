#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_12380_UAS.xml 192.168.55.72:5060 -i 192.168.5.12 -inf testdemo.csv -p 5075 -t t1  -m 1 -aa -trace_msg  -trace_err -r 100000
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_12728_UAS_issue_reproduce.xml 192.168.55.72:5060 -i 192.168.5.12 -inf testdemo.csv -p 5075 -t t1  -m 1 -aa -trace_msg  -trace_err -r 100000
/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_12728_UAS_issue_reproduce.xml 10.133.48.157:5060 -i 10.133.39.159 -inf testdemo.csv -p 5075 -t t1  -m 1 -aa -trace_msg  -trace_err -r 100000
mv ../XML/AURORA_12728_UAS*.log ../SIPP_LOGS/
