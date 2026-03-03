#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_10946_UAC_DO.xml 10.133.48.149:5060 -i 10.133.39.159 -inf test420.csv -p 5075 -t t1 -aa -trace_msg  -trace_err -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_13906_UAS_media.xml 10.133.48.149:5060 -i 10.133.39.159 -inf test420.csv -p 5075 -t t1 -aa -trace_msg  -trace_err -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_10946_UAC_WHR.xml 10.133.48.149:5060 -i 10.133.39.159 -inf test420.csv -p 5075 -t t1 -aa -trace_msg  -trace_err -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_10946_UAC_ONE_AND_TWO.xml 10.133.48.149:5060 -i 10.133.39.159 -inf test420.csv -p 5075 -t t1 -aa -trace_msg  -trace_err -m 1
/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_10946_UAC.xml 10.133.48.238:5060 -i 10.133.39.159 -inf testdemo.csv -p 6025 -t t1 -aa -trace_msg  -trace_err -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14341_UAC_update.xml 10.133.48.235:5060 -i 10.133.39.159 -inf test420.csv -p 5075 -t t1  -aa -trace_msg  -trace_err -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_11996_UAC.xml 10.133.48.149:5060 -i 10.133.39.159 -inf test420.csv -p 5075 -t t1  -aa -trace_msg  -trace_err -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_12485_UAC.xml 10.133.48.235:5060 -i 10.133.39.159 -inf test420.csv -p 5060 -t t2  -aa -trace_msg  -trace_err -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 10.133.39.159 -inf testdemo.csv -p 5061 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.73.53:5060 -i 10.133.39.159 -inf testdemo.csv -p 5061 -t t1  -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.73.26:5060 -i 10.133.39.159 -inf testdemo.csv -p 5061 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml -r 1 -rp 20000 10.133.69.224 -i 10.133.39.159 -inf testdemo.csv -p 5060 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.69.224 -i 10.133.39.159 -inf testdemo.csv -p 5060 -t t1  -aa -trace_msg  -trace_err
mv ../XML/AURORA_10946_UAC*.log ../SIPP_LOGS/
