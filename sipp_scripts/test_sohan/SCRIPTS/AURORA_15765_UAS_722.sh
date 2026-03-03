#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_15765_UAS.xml 192.168.55.79:5060 -i 192.168.5.12 -inf testdemo.csv -p 5088 -m 200 -aa -trace_msg  -trace_err
/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_15765_UAS_exceed_timer.xml 192.168.55.79:5060 -i 192.168.5.12 -inf testdemo.csv -p 5088 -m 200 -aa -trace_msg  -trace_err
mv ../XML/AURORA_15765_UAS*.log ../SIPP_LOGS/
