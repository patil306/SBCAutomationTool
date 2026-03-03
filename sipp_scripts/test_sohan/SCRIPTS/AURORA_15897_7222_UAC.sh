#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.48.87:5060 -i 10.133.39.159 -inf test420.csv -p 5088 -t t2  -aa -trace_msg  -trace_err -m 1
/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_15897_Register_UAC.xml 10.133.48.238:5061 -i 10.133.39.159 -inf test420.csv -p 6028 -t l1  -aa -trace_msg  -trace_err -m 1
mv ../XML/Basic_call_uac*.log ../SIPP_LOGS/
