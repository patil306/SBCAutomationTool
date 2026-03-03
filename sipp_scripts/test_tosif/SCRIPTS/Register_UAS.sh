/home/sipp/sipp.svn/sipp -sf ../XML/Shared_Control_REG_INFO_UAS.xml 192.168.6.148 -i 192.168.6.5 -inf num_time.csv -p 5061 -t l1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_Register_uas.xml 192.168.6.147 -i 192.168.5.12 -inf num1.csv -p 5061 -t l1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_Register_uas.xml 192.168.5.252 -i 192.168.5.12 -inf num1.csv -p 5061 -t l1  -aa -trace_msg  -trace_err
mv ../XML/Shared_Control_REG_INFO_UAS*.log ../SIPP_LOGS/
