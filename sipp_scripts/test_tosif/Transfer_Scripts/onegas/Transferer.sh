#/home/sipp/sipp.svn/sipp -sf ../XML/Transferer.xml 10.133.73.4 -i 10.133.39.159 -inf testdemo.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf transferer_mod6.xml 10.133.73.4 -i 10.133.39.159 -inf testdemo.csv -p 5080 -t t1 
#/home/sipp/sipp.svn/sipp -sf transferer_mod6.xml 192.168.5.223 -i 10.133.39.159 -inf testdemo.csv -p 5063 -t t1 
#/home/sipp/sipp.svn/sipp -sf transferer_mod7.xml 192.168.5.223 -i 192.168.5.12 -inf testdemo.csv -p 5063 -t t1 -aa -trace_msg  -trace_err 
#/home/sipp/sipp.svn/sipp -sf transferor_mod_replace.xml 192.168.32.5 -i 192.168.56.202 -inf testdemo.csv -p 5063 -t t1
/home/sipp/sipp.svn/sipp -sf transferor_mod_rtcp_mux.xml 192.168.32.5 -i 192.168.56.202 -inf testdemo.csv -p 5063 -t t1
#/home/sipp/sipp.svn/sipp -sf transferer_target_Aurora-25530.xml 192.168.5.223 -i 192.168.5.12 -inf testdemo.csv -p 5063 -t t1
#/home/sipp/sipp.svn/sipp -sf transferer_Aurora-25530_1.xml 192.168.5.223 -i 192.168.5.12 -inf testdemo.csv -p 5063 -t t1
#/home/sipp/sipp.svn/sipp -sf transferer_target_Aurora-25530_1.xml 192.168.32.5 -i 192.168.56.202 -inf testdemo.csv -p 5063 -t t1
#/home/sipp/sipp.svn/sipp -sf transferer_mod2.xml 192.168.9.115 -i 192.168.5.12 -inf testdemo.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf transferer_mod2.xml 192.168.9.63 -i 192.168.5.12 -inf testdemo.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.146 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1 -m 1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.5.253 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#mv transferer_*messages.log ../../SIPP_LOGS/
#mv transferer_*errors.log ../../SIPP_LOGS/
