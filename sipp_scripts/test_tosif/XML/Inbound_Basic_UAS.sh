#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_reinvite_call_uas1.xml 10.133.73.4 -i 10.133.39.159 -inf test420.csv -p 5065 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_reinvite_call_uas_vid.xml 10.133.73.4 -i 10.133.39.159 -inf test420.csv -p 5065 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_12485_UAS.xml 10.133.73.4 -i 10.133.39.159 -inf test420.csv -p 5071 -t l1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uas_early.xml 10.133.73.4 -i 10.133.39.159 -inf test420.csv -p 5064 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_reinvite_call_uas1.xml 10.133.69.234 -i 10.133.39.159 -inf test420.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uas.xml 192.168.6.223 -i 192.168.6.5 -inf testdemo2.csv -p 5063 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uas.xml 10.133.73.4 -i 10.133.39.159 -inf testdemo2.csv -p 5080 -t t1
#/home/sipp/sipp.svn/sipp -sf Inbound_reinvite_call_uas_update.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo2.csv -p 5080 -t t1
#/home/sipp/sipp.svn/sipp -sf  Basic_Register_uas_mod1.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo2.csv -p 5080 -t t1
#/home/sipp/sipp.svn/sipp -sf  Basic_Register_uas_mod1.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo2.csv -p 5080 -t t1
#/home/sipp/sipp.svn/sipp -sf  Inbound_reinvite_call_uas_vid1.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo2.csv -p 5080 -t t1
#/home/sipp/sipp.svn/sipp -sf  Inbound_reinvite_call_uas_vid1.xml 10.133.73.4:5061 -i 10.133.39.159 -inf testdemo2.csv -p 5080 -t l1
#/home/sipp/sipp.svn/sipp -sf  AURORA_12485_UAS.xml 10.133.73.4:5061 -i 10.133.39.159 -inf testdemo2.csv -p 5080 -t l1
#/home/sipp/sipp.svn/sipp -sf  AURORA_12485_UAS_3.xml 10.133.73.4:5060 -i 10.133.39.159 -inf testdemo2.csv -p 5080 -t t1
#/home/sipp/sipp.svn/sipp -sf  AURORA_12485_UAS_13_audio.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t t1
#/home/sipp/sipp.svn/sipp -sf  AURORA_17366_UAS.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t u1
#/home/sipp/sipp.svn/sipp -sf   Inbound_Basic_call_uas_prackto1.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t l1
#/home/sipp/sipp.svn/sipp -sf   Inbound_reinvite_call_uas_srtp.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t l1
#/home/sipp/sipp.svn/sipp -sf   Inbound_reinvite_call_uas_inactive.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t t1
#/home/sipp/sipp.svn/sipp -sf   Inbound_reinvite_call_uas_inactive_183.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t t1
#/home/sipp/sipp.svn/sipp -sf   Inbound_Basic_call_uas_info_1.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t t1
#/home/sipp/sipp.svn/sipp -sf   Inbound_Basic_call_uas_info_123.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t t1
#/home/sipp/sipp.svn/sipp -sf   Inbound_reinvite_call_uas_crash.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t t1
#/home/sipp/sipp.svn/sipp -sf   Basic_Options_uas_mod1.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t t1 -m 10
/home/sipp/sipp.svn/sipp -sf   Inbound_Basic_call_uas_sbc.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t t1 -m 10
#/home/sipp/sipp.svn/sipp -sf   Inbound_Basic_call_uas_info.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t t1
#/home/sipp/sipp.svn/sipp -sf   reinvite_out_call_uas_2.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t t1
#/home/sipp/sipp.svn/sipp -sf  AURORA_17366_UAS_12.xml 192.168.8.124:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5067 -t u1
#/home/sipp/sipp.svn/sipp -sf  AURORA_17366_UAS.xml 192.168.8.124:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5067 -t t1
#/home/sipp/sipp.svn/sipp -sf  AURORA_17366_UAS_11.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t u1
#/home/sipp/sipp.svn/sipp -sf  AURORA_17366_UAS_12.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t u1 -r 500
#/home/sipp/sipp.svn/sipp -sf  AURORA_17366_UAS_3.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t u1
#/home/sipp/sipp.svn/sipp -sf  AURORA_12485_UAS_11_audio_basic.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t t1
#/home/sipp/sipp.svn/sipp -sf  AURORA_12485_UAS_11_audio.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t t1
#/home/sipp/sipp.svn/sipp -sf   AURORA_12485_UAS_ANAT.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t t1
#/home/sipp/sipp.svn/sipp -sf   options_uas_test.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t t1
#/home/sipp/sipp.svn/sipp -sf  Basic_Register_uas_mod2.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t t1
#/home/sipp/sipp.svn/sipp -sf  Inbound_uas_vid1.xml 192.168.5.223:5060 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t t1
#/home/sipp/sipp.svn/sipp -sf  AURORA_12485_UAS.xml 192.168.5.223:5061 -i 192.168.5.12 -inf testdemo2.csv -p 5063 -t l1 
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uas_video.xml 192.168.6.223 -i 192.168.6.5 -inf testdemo2.csv -p 5063 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uac.xml 10.133.73.4 -i 10.133.39.159 -inf test420.csv -p 5065 -t t1 -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/uas_prack_BYE_earlydialog_mod.xml 10.133.73.4 -i 10.133.39.159 -inf test420.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uas_auth.xml 10.133.73.4 -i 10.133.39.159 -inf test420.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_5xx_uas_test.xml 10.133.73.4 -i 10.133.39.159 -inf test420.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uas.xml 10.133.73.242 -i 10.133.39.159 -inf test420.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uas.xml 192.168.6.222 -i 192.168.6.5 -inf test420.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uas.xml 10.133.73.52 -i 10.133.39.159 -inf test420.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uas_retrans.xml 10.133.73.52 -i 10.133.39.159 -inf test420.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Inbound_Basic_call_uas.xml 192.168.6.221 -i 192.168.6.5 -inf test420.csv -p 5060 -t t1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.149 -i 192.168.6.5 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.6.146 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1 -m 1  -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/Basic_call_uas.xml 192.168.5.253 -i 192.168.5.12 -inf testdemo.csv -p 5065 -t t1  -aa -trace_msg  -trace_err
#mv ../XML/uas_prack_BYE_earlydialog_mod*.log ../SIPP_LOGS/
#mv ../XML/Inbound_Basic_call_uas*.log ../SIPP_LOGS/
mv ../XML/*.log ../SIPP_LOGS/
