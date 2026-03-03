#/home/sipp/sipp.svn/sipp -sf Inbound_Basic_call_uac.xml 192.168.6.221 -i 192.168.6.5 -inf test420.csv -p 5060 -t t1 -m 1 -aa -trace_msg  -trace_err
/home/sipp/sipp.svn/sipp -sf Inbound_Basic_call_uac.xml 192.168.5.80 -i 192.168.5.12 -inf testdemo_att.csv -p 5060 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf Inbound_Basic_call_uac.xml 192.168.9.115 -i 192.168.5.12 -inf testdemo_att.csv -p 5063 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/delayed_offer.xml 192.168.6.221 -i 192.168.6.5 -inf test420.csv -p 5060 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uac_INFO.xml 192.168.6.221 -i 192.168.6.5 -inf test420.csv -p 5060 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uac_transmit.xml 192.168.6.221 -i 192.168.6.5 -inf test420.csv -p 5060 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.73.53:5060 -i 10.133.39.159 -inf testdemo.csv -p 5061 -t t1  -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.73.26:5060 -i 10.133.39.159 -inf testdemo.csv -p 5061 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml -r 1 -rp 20000 10.133.69.224 -i 10.133.39.159 -inf testdemo.csv -p 5060 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.69.224 -i 10.133.39.159 -inf testdemo.csv -p 5060 -t t1  -aa -trace_msg  -trace_err
mv Inbound_Basic_call_uac*.log ../SIPP_LOGS/
