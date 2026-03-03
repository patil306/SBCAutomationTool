#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.243:5060 -i 192.168.6.5 -inf testdemo.csv -p 5092 -t t1  -m 200 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.243:5060 -i 192.168.6.5 -inf testdemo.csv -p 5095 -t u1  -m 200 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas_withPrack.xml 192.168.6.243:5060 -i 192.168.6.5 -inf testdemo.csv -p 5095 -t u1  -m 200 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas_withPrack.xml 192.168.6.244:5060 -i 192.168.6.5 -inf testdemo.csv -p 5097 -t t1  -m 200 -aa -trace_msg  -trace_err

#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_10419_indailogOption_UAS.xml 192.168.6.243:5060 -i 192.168.6.5 -inf testdemo.csv -p 5096 -t t1  -m 200 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_10419_OutOfDialogOption_UAS.xml 192.168.6.243:5060 -i 192.168.6.5 -inf testdemo.csv -p 5092 -t t1  -m 200 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_10419_indailogOptionAfterACK_UAS.xml 192.168.6.243:5060 -i 192.168.6.5 -inf testdemo.csv -p 5092 -t t1  -m 200 -aa -trace_msg  -trace_err

#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.55.78:5060 -i 192.168.5.12 -inf testdemo.csv -p 5092 -t t1  -m 200 -aa -trace_msg  -trace_err

/home/sipp/sipp.svn/sipp -sf ../XML/attended_Transfer3pcc/Call_user1.xml  10.133.48.83:5060 -i 10.133.39.159 -inf testdemo.csv -p 5093 -t t1  -m 200 -m 1 -aa -trace_msg  -trace_err 


