#xmlfile=`echo $0|sed 's/\.\///' | sed 's/\.[^.]*$//'`
#sipp -i 10.207.23.200 -p 5060 -sf $xmlfile.xml -inf NordStromPriValue-new.csv -max_socket 50000 -l 25000 -m 25000 -t t1 
#sipp -i 10.207.23.200 -p 5061 -sf $xmlfile.xml -inf NordStromPriValue-new.csv -max_socket 50000 -l 25000 -m 25000 -t l1 -tls_cert AvayaSBC.crt -tls_key AvayaSBC.key
#sipp -i 192.168.5.12  -p 6025 -sf NordStromPriRegSubNot.xml 192.168.25.216:5060 -inf NordStromPriValue-new.csv -t u1  -aa -trace_msg  -trace_err
/home/sipp/sipp.svn/sipp -sf Reg_401.xml 192.168.25.216:5060 -i 192.168.5.12 -inf NordStromPriValue-new.csv -p 6025 -t u1  -aa -trace_msg  -trace_err
