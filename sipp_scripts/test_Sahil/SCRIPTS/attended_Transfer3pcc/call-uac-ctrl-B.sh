xmlfile=`echo $0|sed 's/\.\///' | sed 's/\.[^.]*$//'`
#sipp -i 10.135.88.199 -sf $xmlfile.xml -inf value.csv -p 5061 -l 1000 -m 100 -t l1 -tls_cert unencsipera.pem -tls_key unencsipera.key
#/home/sipp/sipp.svn/sipp -i 192.168.5.12 -p 5093 -3pcc 127.0.0.1:4000 -sf ../../XML/attended_Transfer3pcc/call-uac-ctrl-ReferBLeg.xml -inf ../test420.csv -t t1 -m 1 -nd -trace_msg 192.168.55.78:5060

/home/sipp/sipp.svn/sipp -i 10.133.39.159 -p 5093 -3pcc 127.0.0.1:4000 -sf ../../XML/attended_Transfer3pcc/call-uac-ctrl-ReferBLeg.xml -inf ../test420.csv -t t1 -m 1 -nd -trace_msg -trace_err -trace_logs 10.133.48.83:5060
#sipp -i 10.135.88.199 -sf $xmlfile.xml -inf value.csv -p 5060 -nd -trace_msg

#sipp -i 10.135.88.199 -sf $xmlfile.xml -inf value.csv -p 5060 -nd -trace_msg
