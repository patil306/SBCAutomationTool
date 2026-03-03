/home/sipp/sipp.svn/sipp -sf Transfer_Target_mod1.xml 192.168.9.115 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1 -aa -trace_msg  -trace_err

/home/sipp/sipp.svn/sipp -sf transferer_mod1.xml 192.168.9.115 -i 192.168.5.12 -inf testdemo.csv -p 5060 -t t1 -aa -trace_msg  -trace_err

/home/sipp/sipp.svn/sipp -sf Trunk_UAC_mod.xml 10.133.39.197 -i 10.133.39.159 -inf testdemo.csv -p 5060 -t t1 -m 1 -aa -trace_msg  -trace_err

mv ../XML/Transfer_Target*messages.log ../SIPP_LOGS/
mv transferer*messages.log ../SIPP_LOGS/
mv ../XML/Transfer_Target*messages.log ../SIPP_LOGS/
