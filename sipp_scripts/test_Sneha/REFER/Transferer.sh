#/home/sipp/sipp.svn/sipp -sf ../XML/Transferer.xml 10.133.48.83:5060 -i 10.133.39.159 -inf testdemo.csv -p 5092 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Transferer_15509.xml 192.168.55.78:5060 -i 192.168.5.12 -inf testdemo.csv -p 5092 -t t1 -aa -trace_msg  -trace_err -r 5
#/home/sipp/sipp.svn/sipp -sf ../XML/Transferer_15509.xml 192.168.55.80:5060 -i 192.168.5.12 -inf test50002.csv -p 6020 -t t1 -aa -trace_msg  -trace_err -r 5

/home/sipp/sipp.svn/sipp -sf TransfererBlindTransfer.xml 192.168.55.78:5060 -i 192.168.5.12 -inf testdemo.csv -p 5097 -t t1 -aa -trace_msg  -trace_err -m 1

#/home/sipp/sipp.svn/sipp -sf ../XML/Transferer_14488.xml 192.168.55.78:5060 -i 192.168.5.12 -inf testdemo.csv -p 5092 -t t1 -aa -trace_msg  -trace_err -r 5
#/home/sipp/sipp.svn/sipp -sf ../XML/Transferer_14488_722Setup.xml 192.168.6.244:5060 -i 192.168.6.5 -inf testdemo.csv -p 5097 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Transferer_14488_DmitryCase.xml 192.168.6.244:5060 -i 192.168.6.5 -inf testdemo.csv -p 5097 -t t1 -aa -trace_msg  -trace_err

#/home/sipp/sipp.svn/sipp -sf ../XML/Transferer_14488_722SetupGroomingEnabled.xml 192.168.6.244:5060 -i 192.168.6.5 -inf testdemo.csv -p 5099 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.146 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1 -m 1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.5.253 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err

