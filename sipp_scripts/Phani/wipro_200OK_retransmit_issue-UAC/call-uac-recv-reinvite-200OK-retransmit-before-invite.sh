xmlfile=`echo $0|sed 's/\.\///' | sed 's/\.[^.]*$//'`
#sipp -i 10.135.88.200 -sf $xmlfile.xml -inf value.csv 10192.168.151.218 -l 1 -m 1 -nr -t t1 
#sipp -i 10.135.88.200 -p 5060 -sf $xmlfile.xml -inf ../value.csv 10.135.21.2:5060 -r 1 -m 1
sipp -i 10.135.88.200 -p 5060 -sf $xmlfile.xml -inf ../value.csv 10.135.21.2:5060 -r 1 -m 1 -t t1
