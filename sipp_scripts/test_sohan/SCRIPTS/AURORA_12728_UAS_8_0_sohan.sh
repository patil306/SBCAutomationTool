/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_12728_UAS_issue_reproduce.xml 192.168.6.245:5061 -i 192.168.6.5 -inf testdemo.csv -p 5098 -t l1  -m 1 -aa -trace_msg  -trace_err -r 100000
mv ../XML/AURORA_12728_UAS*.log ../SIPP_LOGS/
