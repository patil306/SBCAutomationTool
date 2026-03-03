/home/sipp/sipp.svn/sipp -sf ../XML/Basic_Register_uas.xml 192.168.6.147 -i 192.168.5.12 -inf num1.csv -p 5061 -t l1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_Register_uas.xml 192.168.5.252 -i 192.168.5.12 -inf num1.csv -p 5061 -t l1  -aa -trace_msg  -trace_err
mv ../XML/Basic_Register_uas*.log ../SIPP_LOGS/
