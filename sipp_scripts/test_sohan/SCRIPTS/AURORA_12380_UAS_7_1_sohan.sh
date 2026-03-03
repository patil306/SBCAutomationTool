#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_12380_UAS.xml 192.168.6.243:5060 -i 192.168.6.5 -inf testdemo.csv -p 6001 -t t1  -m 1 -aa -trace_msg  -trace_err -r 100000
/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_12380_UAC.xml 192.168.6.243:5060 -i 192.168.6.5 -inf testdemo.csv -p 6001 -t t1  -m 1 -aa -trace_msg  -trace_err -m 1
mv ../XML/AURORA_12380_UAS*.log ../SIPP_LOGS/
