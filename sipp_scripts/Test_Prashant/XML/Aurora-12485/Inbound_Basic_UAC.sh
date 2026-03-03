#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uac.xml 192.168.6.221 -i 192.168.6.5 -inf test420.csv -p 5060 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uac_auth.xml 192.168.6.223 -i 192.168.6.5 -inf test420.csv -p 5060 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uac.xml 192.168.6.223 -i 192.168.6.5 -inf test420.csv -p 5060 -t t1 -m 27 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uac.xml 192.168.6.223 -i 192.168.6.5 -inf test420.csv -p 5063 -t t1 -r 7 -rp 2000 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uac.xml 10.133.73.4:5060 -i 10.133.39.159 -inf test420.csv -p 5080 -t t1 -m 1 -rp 2000 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uac.xml 192.168.6.223:5060 -i 192.168.6.5 -inf testdemo2.csv -p 5063 -t t1 -m 1 -rp 2000
#/home/sipp/sipp.svn/sipp -sf Inbound_reinvite_call_uac_update.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t t1 -m 1 -rp 2000
#/home/sipp/sipp.svn/sipp -sf Basic_Register_uac_mod1.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t t1 -m 1 -rp 2000
#/home/sipp/sipp.svn/sipp -sf Inbound_reinvite_call_uac_vid1.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t t1 -m 1 -rp 2000
#/home/sipp/sipp.svn/sipp -sf Inbound_reinvite_call_uac_vid1.xml 192.168.5.223:5061 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t l1 -m 1 -rp 2000
#/home/sipp/sipp.svn/sipp -sf AURORA_12485_UAC.xml 192.168.5.223:5061 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t l1 -m 1 -rp 2000
#/home/sipp/sipp.svn/sipp -sf AURORA_12485_UAC_3.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t t1 -m 1 -rp 2000
#/home/sipp/sipp.svn/sipp -sf AURORA_12485_UAC_3.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo2.csv -p 5080 -t t1 -m 1 -rp 2000
#/home/sipp/sipp.svn/sipp -sf Inbound_uac_vid1.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo2.csv -p 5080 -t t1 -m 1 -rp 2000
#/home/sipp/sipp.svn/sipp -sf AURORA_12485_UAC_5.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo2.csv -p 5080 -t t1 -m 1 -rp 2000
#/home/sipp/sipp.svn/sipp -sf AURORA_12485_UAC_11_audio_basic.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo2.csv -p 5080 -t t1 -m 1 -rp 2000
#/home/sipp/sipp.svn/sipp -sf AURORA_12485_UAC_11_audio.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo2.csv -p 5080 -t t1 -m 1 -rp 2000
#/home/sipp/sipp.svn/sipp -sf AURORA_17366_UAC_2.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo2.csv -p 5080  -m 1 -t u1 -rp 2000
/home/sipp/sipp.svn/sipp -sf AURORA_17366_UAC.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo2.csv -p 5080  -m 1 -t u1 -rp 2000
#/home/sipp/sipp.svn/sipp -sf AURORA_17366_UAC_13.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo2.csv -p 5080  -m 500 -t u1 -rp 1000 -l 2
#/home/sipp/sipp.svn/sipp -sf AURORA_17366_UAC_12.xml 10.133.39.61:5060 -i 10.133.39.159 -inf testdemo2.csv -p 5089  -m 1 -t u1 -rp 1000
#/home/sipp/sipp.svn/sipp -sf AURORA_17366_UAC.xml 10.133.39.61:5060 -i 10.133.39.159 -inf testdemo2.csv -p 5089  -m 1 -t t1 -rp 1000
#/home/sipp/sipp.svn/sipp -sf AURORA_17366_UAC_11.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo2.csv -p 5080  -m 1 -t u1 -rp 1000
#/home/sipp/sipp.svn/sipp -sf AURORA_12485_UAC_ANAT_1.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo2.csv -p 5080 -t t1 -m 1 -rp 2000
#/home/sipp/sipp.svn/sipp -sf options_uac_test.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo2.csv -p 5080 -t t1 -m 1 -rp 2000
#/home/sipp/sipp.svn/sipp -sf AURORA_12485_UAC.xml 10.133.73.4:5061 -i 10.133.39.159 -inf testdemo2.csv -p 5080 -t l1 -m 1 -rp 2000
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uac_video.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo2.csv -p 5080 -t t1 -m 1 -rp 2000 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uac.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo2.csv -p 5080 -t t1 -m 1 -rp 2000 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uas.xml 192.168.6.223 -i 192.168.6.5 -inf test420.csv -p 5063 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_reinvite_call_uac2.xml 192.168.6.223 -i 192.168.6.5 -inf test420.csv -p 5063 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_reinvite_call_uac_vid.xml 192.168.6.223 -i 192.168.6.5 -inf test420.csv -p 5063 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_12485_UAC.xml 192.168.6.223:5061 -i 192.168.6.5 -inf test420.csv -p 5073 -t l1 -m 1 -aa -trace_msg  -trace_err

#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_12485_UAC.xml 192.168.6.223 -i 192.168.6.5 -inf test420.csv -p 5073 -t l1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uac_early.xml 192.168.6.223 -i 192.168.6.5 -inf test420.csv -p 5063 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/scrubber.xml 192.168.6.223 -i 192.168.6.5 -inf test420.csv -p 5063 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_reinvite_call_uac2.xml 192.168.10.155 -i 192.168.5.12 -inf test420.csv -p 5060 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_reinvite_call_uac2.xml 192.168.9.53 -i 192.168.5.12 -inf test420.csv -p 5060 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Outbound_UAC_Test_1_mod.xml 192.168.6.223 -i 192.168.6.5 -inf test420.csv -p 5060 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uac.xml 10.133.73.241 -i 10.133.39.159 -inf test420.csv -p 5060 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/delayed_offer.xml 192.168.6.221 -i 192.168.6.5 -inf test420.csv -p 5060 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uac_INFO.xml 192.168.6.221 -i 192.168.6.5 -inf test420.csv -p 5060 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uac_transmit.xml 192.168.6.221 -i 192.168.6.5 -inf test420.csv -p 5060 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.73.53:5060 -i 10.133.39.159 -inf testdemo.csv -p 5061 -t t1  -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.73.26:5060 -i 10.133.39.159 -inf testdemo.csv -p 5061 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml -r 1 -rp 20000 10.133.69.224 -i 10.133.39.159 -inf testdemo.csv -p 5060 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uac.xml 10.133.69.224 -i 10.133.39.159 -inf testdemo.csv -p 5060 -t t1  -aa -trace_msg  -trace_err
#mv ../XML/Outbound_UAC_Test_1_mod*.log ../SIPP_LOGS/
#mv ../XML/Inbound_Basic_call_uac*.log ../SIPP_LOGS/
mv ../XML/Inbound_reinvite_call_uac*.log ../SIPP_LOGS/
