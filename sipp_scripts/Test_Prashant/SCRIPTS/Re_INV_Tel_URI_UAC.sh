/home/sipp/sipp.svn/sipp -sf ../XML/Re_INV_Tel_URI_UAC.xml 10.133.39.200:5060 -i 10.133.39.159 -inf testdemo.csv -p 5066 -t t1  -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Tel_URI_UAC.xml 10.133.73.26:5060 -i 10.133.39.159 -inf testdemo.csv -p 5066 -t t1  -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.73.26:5060 -i 10.133.39.159 -inf testdemo.csv -p 5061 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml -r 1 -rp 20000 10.133.69.224 -i 10.133.39.159 -inf testdemo.csv -p 5060 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.69.224 -i 10.133.39.159 -inf testdemo.csv -p 5060 -t t1  -aa -trace_msg  -trace_err
mv ../XML/Re_INV_Tel_URI_UAC*.log ../SIPP_LOGS/
