#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_18033_UAS.xml 192.168.55.79:5060 -i 192.168.5.12 -inf testdemo.csv -p 5097 -m 200 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf AURORA_18033_UAS_testcase41.xml 192.168.55.140:5060 -i 192.168.5.12 -inf testdemo.csv -p 5088 -m 200 -t u1
/home/sipp/sipp.svn/sipp -sf AURORA_18033_UAS_reproduce.xml 192.168.55.140:5060 -i 192.168.5.12 -inf testdemo.csv -p 5088 -m 200 -t u1
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_18033_UAS_reproduce.xml 192.168.55.79:5060 -i 192.168.5.12 -inf testdemo.csv -p 5097 -m 200 -aa -trace_msg  -trace_err
mv ../XML/AURORA_18033_UAS_*.log ../SIPP_LOGS/
