/home/sipp/sipp.svn/sipp -sf ../XML/Trunk_Invite-External_Internal_UAC_SIPREC.xml 10.133.73.26:5060 -i 10.133.39.159 -inf testdemo.csv -p 5061 -t t1  -m 1 -aa -trace_msg  -trace_err
#/root/sipp.svn/sipp -sf ../XML/Trunk_Invite-External_Internal_UAC_SIPREC_SRTP.xml 10.133.39.177:5061 -i 10.133.36.8 -inf testdemo.csv -t ln -m 1 -aa -trace_msg  -trace_err
mv Trunk_*.log ../SIPP_LOGS/
