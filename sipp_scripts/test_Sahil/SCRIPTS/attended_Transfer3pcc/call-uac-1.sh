#/home/sipp/sipp.svn/sipp -i 10.133.5.12 -p 5092 -sf ../../XML/attended_Transfer3pcc/call-uac-refertoreinvite.xml -inf ../test420.csv 192.168.55.78:5060 -l 1 -m 1 -t t1 
/home/sipp/sipp.svn/sipp -i 10.133.5.12 -p 5092 -sf ../../XML/Basic_call_uas.xml -inf ../test420.csv 192.168.55.78:5060 -l 1 -m 1 -aa -trace_msg  -trace_err 
#/home/sipp/sipp.svn/sipp -sf ../../XML/attended_Transfer3pcc/Call_user1.xml 10.133.48.83:5060 -i 10.133.39.159 -inf ../test420.csv -p 5092 -t t1 -m 1 -aa -trace_msg  -trace_err 
#/home/sipp/sipp.svn/sipp -sf ../../XML/Basic_call_uac.xml 10.133.48.83:5060 -i 10.133.39.159 -inf ../test420.csv -p 5092 -t t1 -m 1 -aa -trace_msg  -trace_err 
#sipp -i 10.135.88.200 -sf $xmlfile.xml -inf value.csv 10.135.21.86 -l 1 -m 1 -nr

