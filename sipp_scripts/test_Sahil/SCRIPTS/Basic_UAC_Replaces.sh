#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.48.83:5060 -i 10.133.39.159 -inf test420.csv -p 5092 -t t1  -aa -trace_msg  -trace_err -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.48.85:5060 -i 10.133.39.159 -inf test420.csv -p 5097 -t t1  -aa -trace_msg  -trace_err -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_10419_indailogOption_UAC.xml 10.133.48.83:5060 -i 10.133.39.159 -inf test420.csv -p 5092 -t t1  -aa -trace_msg  -trace_err -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/uac_XeroxCore_replaces.xml 10.133.48.83:5060 -i 10.133.39.159 -inf test40006.csv -p 5092 -t u1  -aa -trace_msg  -trace_err -m 1

#/home/sipp/sipp.svn/sipp -sf ../XML/uac_XeroxCore_replaces_ReplaceUAC.xml 10.133.48.83:5060 -i 10.133.39.159 -inf test40006.csv -p 5092 -t u1  -aa -trace_msg  -trace_err -m 1

#/home/sipp/sipp.svn/sipp -sf ../XML/uac_XeroxCore_replaces_ReplaceUAC.xml 192.168.9.82:5060 -i 192.168.5.12 -inf test40006.csv -p 5096 -t u1  -aa -trace_msg  -trace_err -m 1

#/home/sipp/sipp.svn/sipp -sf ../XML/uac_XeroxCore_replaces_ReplaceUAC.xml 192.168.55.78:5060 -i 192.168.5.12 -inf test40006.csv -p 5092 -t u1  -aa -trace_msg  -trace_err -m 1

/home/sipp/sipp.svn/sipp -sf ../XML/uac_XeroxCore_replaces_ReplaceUAC.xml 10.133.48.83:5060 -i 10.133.39.159 -inf test40006.csv -p 5098 -t u1  -aa -trace_msg  -trace_err -m 1

#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_10419_OutOfDialogOption_UAC.xml 10.133.48.83:5060 -i 10.133.39.159 -inf test420.csv -p 5092 -t t1  -aa -trace_msg  -trace_err -m 1

#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_10419_indailogOptionAfterACK_UAC.xml 10.133.48.83:5060 -i 10.133.39.159 -inf test420.csv -p 5092 -t t1  -aa -trace_msg  -trace_err -m 1

#/home/sipp/sipp.svn/sipp -sf /home/sipp/test_Sneha/XML/uac_XeroxCore_replaces.xml 10.133.48.238:5060 -i 10.133.39.159 -inf test50001.csv -p 5090 -t t1 -aa -trace_msg  -trace_err -m 1

mv ../XML/Basic_call_uac*.log ../SIPP_LOGS/
