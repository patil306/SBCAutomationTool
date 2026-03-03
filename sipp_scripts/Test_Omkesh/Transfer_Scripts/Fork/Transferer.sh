#/home/sipp/sipp.svn/sipp -sf ../XML/Transferer.xml 10.133.73.4 -i 10.133.39.159 -inf testdemo.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf transferer_mod_prack2.xml 10.133.73.4 -i 10.133.39.159 -inf testdemo.csv -p 5080 -t t1 -aa -trace_msg  -trace_err
/home/sipp/sipp.svn/sipp -sf transferer_mod_prack3.xml 10.133.73.4 -i 10.133.39.159 -inf testdemo.csv -p 5080 -t t1
#/home/sipp/sipp.svn/sipp -sf transferer_mod_prack.xml 10.133.48.157 -i 10.133.39.159 -inf testdemo.csv -p 5075 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp_fax/sipp -sf transferer_mod_fax.xml 10.133.73.4 -i 10.133.39.159 -inf testdemo.csv -p 5080 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp_fax/sipp -sf transferer_mod2.xml 135.20.28.60 -i 10.133.39.159 -inf testdemo.csv -p 5080 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf transferer_mod2.xml 192.168.9.115 -i 192.168.5.12 -inf testdemo.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf transferer_mod2.xml 192.168.9.63 -i 192.168.5.12 -inf testdemo.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.146 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1 -m 1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.5.253 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
mv transferer_*messages.log ../../SIPP_LOGS/
mv transferer_*errors.log ../../SIPP_LOGS/
