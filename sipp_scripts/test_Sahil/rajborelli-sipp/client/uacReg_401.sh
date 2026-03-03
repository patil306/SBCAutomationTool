#xmlfile=`echo $0|sed 's/\.\///' | sed 's/\.[^.]*$//'`
#sipp -i 10.0.11.2 -sf $xmlfile.xml -inf value.csv 10.0.11.251 -l 1 -m 1 -nr -t t1 
#sipp -i 10.0.51.2 -sf $xmlfile.xml -inf value.csv 10.0.51.251 -l 1 -m 1 -nr -t t1 
#sipp -i 10.207.23.199 -sf $xmlfile.xml -inf NordStromPriValue-New.csv 10.81.23.89 -r 10 -rp 30s -m 10000000 -nr -t t1 
#sipp -i 10.207.23.199 -p 5061 -sf $xmlfile.xml -inf NordStromPriValue-New.csv 10.81.23.90:5061 -r 1 -m 1 -l 1 -t l1 -tls_cert new_client.crt -tls_key new_client.key
/home/sipp/sipp.svn/sipp -sf uacReg_401.xml 10.133.48.218:5060 -i 10.133.39.159 -inf NordStromPriValue-New.csv -p 6021 -t u1 -m 1 -aa -trace_msg  -trace_err -r 1
