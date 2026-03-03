/home/sipp/sipp.svn/sipp -sf ../XML/18x_No_Sdp_UAC_SIPREC_Forking_7.1.xml  10.133.73.53:5060 -i 10.133.39.159 -inf testdemo.csv -p 5061 -t t1  -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Trunk_Invite-External_Internal_UAC_SIPREC_7.1.xml 10.133.73.51:5060 -i 10.133.39.159 -inf testdemo.csv -p 5061 -t t1  -m 1 -aa -trace_msg  -trace_err
# SBC-7-1 config /home/sipp/sipp.svn/sipp -sf ../XML/Trunk_Invite-External_Internal_UAC_SIPREC_7.1.xml 10.133.73.39:5060 -i 10.133.39.159 -inf testdemo.csv -p 5061 -t t1  -m 1 -aa -trace_msg  -trace_err
#/root/sipp.svn/sipp -sf ../XML/Trunk_Invite-External_Internal_UAC_SIPREC_SRTP.xml 10.133.39.177:5061 -i 10.133.36.8 -inf testdemo.csv -t ln -m 1 -aa -trace_msg  -trace_err
mv ../XML/18x_No_Sdp_UAS_SIPREC_Forking_7.1_*messages.log ../SIPP_LOGS/
