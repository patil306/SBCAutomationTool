/home/sipp/sipp.svn/sipp -sf ../XML/Transfer_Target.xml 192.168.55.79 -i 192.168.5.12 -inf testdemo.csv -p 6020 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Transfer_SCRIPTS/Transfer_Target_mod6_anat.xml 192.168.55.79 -i 192.168.5.12 -inf testdemo.csv -p 6025 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Transfer_SCRIPTS/Transfer_Target_mod6_anat.xml 192.168.55.75 -i 192.168.5.12 -inf testdemo.csv -p 6020 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.146 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1 -m 1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.5.253 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
mv ../XML/Transfer_Target*messages.log ../SIPP_LOGS/
