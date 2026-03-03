xmlfile=`echo $0|sed 's/\.\///' | sed 's/\.[^.]*$//'`
sipp -i 10.135.88.200 -sf $xmlfile.xml -inf value.csv 10.135.21.19 -l 1 -m 1 -nr
#sipp -i 10.135.88.200 -sf $xmlfile.xml -inf value.csv 10.135.21.86 -l 1 -m 1 -nr
