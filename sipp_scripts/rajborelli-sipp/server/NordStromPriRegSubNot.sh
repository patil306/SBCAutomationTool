xmlfile=`echo $0|sed 's/\.\///' | sed 's/\.[^.]*$//'`
#sipp -i 10.207.23.200 -p 5060 -sf $xmlfile.xml -inf NordStromPriValue-new.csv -max_socket 50000 -l 25000 -m 25000 -t t1 
sipp -i 10.207.23.200 -p 5061 -sf $xmlfile.xml -inf NordStromPriValue-new.csv -max_socket 50000 -l 25000 -m 25000 -t l1 -tls_cert AvayaSBC.crt -tls_key AvayaSBC.key
