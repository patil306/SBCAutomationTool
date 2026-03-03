#/home/sipp/sipp.svn/sipp -sf ../XML/Trunk_UAC.xml 192.168.6.222 -i 192.168.6.5 -inf testdemo.csv -p 5075 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf Trunk_UAC_BYEphani.xml 192.168.6.223:5060 -i 192.168.6.5 -inf testdemo.csv -p 5063 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf Trunk_UAC_mod4.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo.csv -p 5063 -t t1 -m 1
#/home/sipp/sipp.svn/sipp -sf Trunk_UAC_mod4.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo.csv -p 5080 -t t1 -m 1
#/home/sipp/sipp.svn/sipp -sf Trunk_UAC_mod6_delayed.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo.csv -p 5080 -t t1 -m 1
#/home/sipp/sipp.svn/sipp -sf Trunk_UAC_mod_replace3.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo.csv -p 5080 -t t1 -m 1
#/home/sipp/sipp.svn/sipp -sf Trunk_UAC_mod_replace4.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo.csv -p 5080 -t t1 -m 1
/home/sipp/sipp.svn/sipp -sf Inbound_Basic_call_uac.xml 10.133.36.32 -i 10.133.39.159 -inf testdemo.csv -p 5072 -t t1 -m 1
#/home/sipp/sipp.svn/sipp -sf Trunk_UAC_mod_busy.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo.csv -p 5080 -t u1 -m 1
#/home/sipp/sipp.svn/sipp -sf Trunk_UAC_mod_busy.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo.csv -p 5080 -t u1 -m 1
#/home/sipp/sipp.svn/sipp -sf Trunk_UAC_mod_replace3.xml 10.133.48.238:5060 -i 10.133.39.159 -inf testdemo.csv -p 5088 -t t1 -m 1
#/home/sipp/sipp.svn/sipp -sf Trunk_UAC_mod_busy.xml 10.133.48.238:5060 -i 10.133.39.159 -inf testdemo.csv -p 5088 -t t1 -m 1
#/home/sipp/sipp.svn/sipp -sf Trunk_UAC_mod_replace.xml 10.133.48.59:5060 -i 10.133.39.159 -inf testdemo.csv -p 5060 -t t1 -m 1
#/home/sipp/sipp.svn/sipp -sf Trunk_UAC_mod_replace.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo.csv -p 5063 -t t1 -m 1
#/home/sipp/sipp.svn/sipp -sf Trunk_UAC_mod4.xml 192.168.6.223:5060 -i 192.168.6.5 -inf testdemo.csv -p 5063 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf Trunk_UAC_mod1.xml 10.133.39.197 -i 10.133.39.159 -inf testdemo.csv -p 5060 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf Trunk_UAC_mod1.xml 10.133.69.201 -i 10.133.39.159 -inf testdemo.csv -p 5060 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.146 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1 -m 1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.5.253 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
