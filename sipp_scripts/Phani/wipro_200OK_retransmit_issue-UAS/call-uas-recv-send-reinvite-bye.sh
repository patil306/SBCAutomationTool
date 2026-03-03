xmlfile=`echo $0|sed 's/\.\///' | sed 's/\.[^.]*$//'`
#sipp -i 10.135.88.199 -sf $xmlfile.xml -inf value.csv -p 5061 -l 1000 -m 100 -t l1 -tls_cert unencsipera.pem -tls_key unencsipera.key
#sipp -i 10.135.88.198 -sf $xmlfile.xml -inf value.csv -p 5060 -nd -trace_msg
sipp -i 10.135.88.199 -sf $xmlfile.xml -inf ../value.csv -p 5060 -t t1 
//sipp -i 10.135.88.199 -sf $xmlfile.xml -inf ../value.csv -p 5060  
