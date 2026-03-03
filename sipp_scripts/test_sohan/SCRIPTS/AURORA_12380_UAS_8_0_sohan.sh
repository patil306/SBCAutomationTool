/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_12380_UAS.xml 192.168.6.245:5060 -i 192.168.6.5 -inf testdemo.csv -p 5097 -t t1  -m 1 -aa -trace_msg  -trace_err -r 100000
mv ../XML/AURORA_12380_UAS*.log ../SIPP_LOGS/
