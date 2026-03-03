#/home/sipp/sipp-3.3.990/sipp -sf basic_uas_rec.xml 192.168.9.78:5060 -i 192.168.9.93 -p 5060 -t u1 -m 1
#/home/sipp/sipp-3.3.990/sipp -sf tsystem-xfer-uas.xml -inf testdemo.csv 192.168.9.82:5060 -i 192.168.9.93 -p 5060 -t u1 -m 100 # for attended transfer scenario
#/home/sipp/sipp-3.3.990/sipp -sf uas-nullInvite.xml -inf testdemo.csv 192.168.9.82:5060 -i 192.168.9.93 -p 5060 -t t1 -m 100 # for attended transfer scenario
#/home/sipp/sipp-3.3.990/sipp -sf uas-nullInvite.xml -inf testdemo.csv 192.168.9.170:5060 -i 192.168.9.93 -p 5060 -t t1 -m 100 # for attended transfer scenario
#/home/sipp/sipp-3.3.990/sipp -sf basic_uas_DNSCrash.xml -inf testdemo.csv 10.133.39.193:5060 -i 10.133.39.199 -p 5060 -t u1 -m 10 # upKar's 8.x SBCE
#/home/sipp/sipp-3.3.990/sipp -sf basic_uas_orig.xml -inf testdemo.csv 192.168.5.90:5060 -i 192.168.9.30 -p 5060 -t u1 -m 100 # Merina 8.x SBCE
#/home/sipp/sipp-3.3.990/sipp -sf cm-update-uas2.xml -inf testdemo.csv 10.133.39.193:5060 -i 10.133.39.199 -p 5060 -t t1 -m 10 # Merina 8.x SBCE
#/home/sipp/sipp-3.3.990/sipp -sf uas-nullInvite.xml -inf testdemo.csv 10.133.39.182:5060 -i 10.133.39.199 -p 5060 -t u1 -m 10


# 7.x
#/home/sipp/sipp-3.3.990/sipp -sf boschStuckCall-UAS.xml -inf testdemo.csv 10.133.39.182:5061 -i 10.133.39.199 -p 5061 -t l1  -tls_cert ./DBSSL_Certs/server.crt -tls_key ./DBSSL_Certs/server.key
#/home/sipp/sipp-3.3.990/sipp -sf delayedHandling-uas.xml -inf testdemo.csv 10.133.39.182:5061 -i 10.133.39.199 -p 5060 -t t1 -m 10
#/home/sipp/sipp-3.3.990/sipp -sf uas_akash.xml -inf testdemo.csv 10.133.39.182:5060 -i 10.133.39.199 -p 5060 -t t1  -m 1

# 8.x SIPp-UAS
#/home/sipp/sipp-3.3.990/sipp -sf recorder-uas.xml -inf testdemo.csv 10.133.39.192:5060 -i 10.133.39.199 -p 5060 -t t1 -m 10 # upkar 8.1 SBCE

/home/sipp/sipp.svn/sipp -sf /home/sipp/test_Sahil/XML/180Fork_uas_216.xml 192.168.25.216:5060 -i 192.168.5.12 -inf test50003.csv -p 6025 -t u1  -aa -trace_msg  -trace_err


#/home/sipp/sipp-3.3.990/sipp -sf 401-glare-uas.xml -inf testdemo.csv 10.133.39.192:5060 -i 10.133.39.199 -p 5060 -t t1 -m 10 # upkar 8.1 SBCE
