#/root/phani/sipp.svn/sipp -sf tsystem-xfer-uac.xml -inf testdemo.csv 10.133.39.182 -inf testdemo.csv -i 10.133.39.191 -p 5060 -t u1 -m 1 #for transfert scenario
#/root/phani/sipp.svn/sipp -sf uac-nullInvite.xml 10.133.39.182 -inf testdemo.csv -i 10.133.39.191 -p 5060 -t t1 -m 1 # Merina 8.x SBCE
#/root/phani/sipp.svn/sipp -sf uac-options.xml 10.133.39.192 -inf testdemo.csv -i 10.133.39.191 -p 5060 -t t1 -m 1 # Merina 8.x SBCE
#/root/phani/sipp.svn/sipp -sf cm-update-uac.xml 10.133.39.193 -inf testdemo.csv -i 10.133.39.191 -p 5060 -t t1 -m 1 # Merina 8.x SBCE
#/root/phani/sipp.svn/sipp -sf routing-test-UAC.xml 192.168.9.192 -inf testdemo.csv -i 192.168.9.30 -p 5060 -t u1 -m 1



## 7.x SIPp UAC
#/root/phani/sipp.svn/sipp -sf boschStuckCall-UAC.xml 192.168.9.82:5061 -inf testdemo.csv -i 192.168.9.30 -p 5061 -t l1 -m 1 -nd -tls_cert ./DBSSL_Certs/server.crt -tls_key ./DBSSL_Certs/server.key
#/root/phani/sipp.svn/sipp -sf delayedHandling-UAC.xml 192.168.9.82:5061 -inf testdemo.csv -i 192.168.9.30 -p 5061 -t l1 -m 1 -nd -tls_cert ./DBSSL_Certs/server.crt -tls_key ./DBSSL_Certs/server.key
#/root/phani/sipp.svn/sipp -sf uac_akash.xml 192.168.9.82:5060 -inf testdemo.csv -i 192.168.9.30 -p 5060 -t t1 -m 1 

#8.1.x SIPpUAC
#/root/phani/sipp.svn/sipp -sf recorder_UAC.xml 192.168.9.192 -inf testdemo.csv -i 192.168.9.30 -p 5060 -t t1 -m 1 # upkar 8.x SBCE


#/root/phani/sipp.svn/sipp -sf 401-glare-uac.xml 192.168.9.192 -inf testdemo.csv -i 192.168.9.30 -p 5060 -t t1 -m 1 # upkar 8.x SBCE


/home/sipp/sipp.svn/sipp -sf /home/sipp/test_Sahil/XML/reInviteSimple_uac_216.xml 10.133.48.218:5060 -i 10.133.39.159 -inf test50003.csv -p 6021 -t u1 -m 1 -aa -trace_msg  -trace_err -r 1

#/root/phani/sipp.svn/sipp -sf Basic_Options_uas_mod1.xml 192.168.9.82 -inf testdemo.csv -i 192.168.9.30 -p 5060 -t t1 -m 1 # upkar 8.x SBCE
