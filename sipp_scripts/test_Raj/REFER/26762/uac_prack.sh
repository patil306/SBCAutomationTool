#/home/sipp/sipp.svn/sipp -sf ../XML/Trunk_UAC.xml 192.168.6.243:5060 -i 192.168.6.5 -inf testdemo.csv -p 5092 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Trunk_UAC.xml 10.133.48.83:5060 -i 10.133.39.159 -inf testdemo.csv -p 5094 -t t1 -aa -trace_msg  -trace_err -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/Trunk_UAC_BlindTransferDelayedOffer.xml 10.133.48.83:5060 -i 10.133.39.159 -inf testdemo.csv -p 5094 -t t1 -aa -trace_msg  -trace_err -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/Trunk_UAC_BlindTransferDelayedOffer.xml 10.133.48.168:5060 -i 10.133.39.159 -inf test50001.csv -p 6004 -t t1 -aa -trace_msg  -trace_err -m 1

/home/sipp/sipp.svn/sipp -sf uac_prack.xml 192.168.55.74:5062 -i 192.168.5.12 -inf testdemo.csv -p 5096  -aa -trace_msg  -trace_err -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/Trunk_UAC_BlindTransferDelayedOffer_15090.xml 10.133.48.83:5060 -i 10.133.39.159 -inf testdemo.csv -p 5094 -t t1 -aa -trace_msg  -trace_err -m 1

#/home/sipp/sipp.svn/sipp -sf ../XML/Trunk_UAC.xml 10.133.48.85:5060 -i 10.133.39.159 -inf testdemo.csv -p 5097 -t u1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Transferee_14488_DmitryCase.xml 10.133.48.85:5060 -i 10.133.39.159 -inf testdemo.csv -p 5097 -t u1 -m 1 -aa -trace_msg  -trace_err

#/home/sipp/sipp.svn/sipp -sf ../XML/Trunk_UAC.xml 10.133.48.85:5060 -i 10.133.39.159 -inf testdemo.csv -p 5099 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Trunk_UAC.xml 10.133.48.85:5060 -i 10.133.39.159 -inf testdemo.csv -p 5099 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.73.53:5060 -i 10.133.39.159 -inf testdemo.csv -p 5061 -t t1  -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.73.26:5060 -i 10.133.39.159 -inf testdemo.csv -p 5061 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml -r 1 -rp 20000 10.133.69.224 -i 10.133.39.159 -inf testdemo.csv -p 5060 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.69.224 -i 10.133.39.159 -inf testdemo.csv -p 5060 -t t1  -aa -trace_msg  -trace_err
