#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_13906_UAC_media.xml 192.168.6.242:5060 -i 192.168.6.5 -inf test420.csv -p 5075 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_10946_UAS_WHR.xml 192.168.6.242:5060 -i 192.168.6.5 -inf test420.csv -p 5075 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_10946_UAS_ONE.xml 192.168.6.242:5060 -i 192.168.6.5 -inf test420.csv -p 5075 -t t1 -m 1 -aa -trace_msg  -trace_err
/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_10946_UAS.xml 192.168.6.242:5060 -i 192.168.6.5 -inf test420.csv -p 5075 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14341_UAS_update.xml 192.168.6.240:5060 -i 192.168.6.5 -inf test420.csv -p 5075 -t t1  -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14341_UAS.xml 192.168.6.240:5060 -i 192.168.6.5 -inf test420.csv -p 5075 -t t1  -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_11996_UAS.xml 192.168.6.242 -i 192.168.6.5 -inf test420.csv -p 5075 -t t1  -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_12485_UAS.xml 192.168.6.246:5060 -i 192.168.6.5 -inf test420.csv -p 5060 -t t1  -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.146 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1 -m 1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.5.253 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
mv ../XML/AURORA_10946_UAS*.log ../SIPP_LOGS/
