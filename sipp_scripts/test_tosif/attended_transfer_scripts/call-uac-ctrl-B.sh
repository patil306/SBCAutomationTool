xmlfile=`echo $0|sed 's/\.\///' | sed 's/\.[^.]*$//'`
#sipp -i 10.135.88.199 -sf $xmlfile.xml -inf value.csv -p 5061 -l 1000 -m 100 -t l1 -tls_cert unencsipera.pem -tls_key unencsipera.key
sipp -i 10.135.88.200 -p 5060 -3pcc 127.0.0.1:4000 -sf $xmlfile.xml -inf ctrl_values.csv -nd -trace_msg 10.135.21.77:5060

#sipp -i 10.135.88.199 -sf $xmlfile.xml -inf value.csv -p 5060 -nd -trace_msg

#sipp -i 10.135.88.199 -sf $xmlfile.xml -inf value.csv -p 5060 -nd -trace_msg
