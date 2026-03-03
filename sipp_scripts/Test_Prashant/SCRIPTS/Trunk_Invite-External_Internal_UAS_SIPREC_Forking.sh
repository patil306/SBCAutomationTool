/home/sipp/sipp.svn/sipp -sf ../XML/Trunk_Invite-External_Internal_UAS_SIPREC_Forking.xml 192.168.5.253 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Trunk_Invite-External_Internal_UAS_SIPREC.xml 192.168.5.32 -i 192.168.5.12 -inf testdemo.csv -p 5061 -t ln  -m 1 -aa -trace_msg  -trace_err
mv trunk_*.log ../SIPP_LOGS/
