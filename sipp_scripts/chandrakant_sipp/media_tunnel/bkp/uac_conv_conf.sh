#!/bin/bash
#/home/sipp/sipp.svn/sipp -sf /home/sipp/Test_Shobhit/SCRIPTS/ConvConfScripts/UAC_REINVITE_TLS_CONV_CONF.xml 10.133.39.176:5061 -i 10.133.39.159 -p 5061 -t l1  -m 1 -aa -trace_msg  -trace_err -inf /home/sipp/Test_Shobhit/SCRIPTS/ConvConfScripts/UAS_Conv_Conf_RTP_SRTP.csv -t l1 
/home/sipp/sipp.svn/sipp -sf UAC_REINVITE_TLS_CONV_CONF.xml 192.168.6.146:5061 -i 192.168.6.5 -p 5061 -t l1  -m 1 -aa -trace_msg  -trace_err -inf UAS_Conv_Conf_RTP_SRTP.csv -t l1 
#/home/sipp/sipp.svn/sipp -sf UAC_REINVITE_TLS_CONV_CONF.xml 192.168.6.223:5061 -i 192.168.6.5 -p 5061 -t l1  -m 10000 -aa -trace_msg  -trace_err -inf UAS_Conv_Conf_RTP_SRTP.csv -t l1 
#/home/sipp/sipp.svn/sipp -sf /home/sipp/Test_Shobhit/SCRIPTS/ConvConfScripts/UAC_CONV_CONF.xml 10.133.39.176:5061 -i 10.133.39.159 -p 5061 -t l1  -m 1 -aa -trace_msg  -trace_err -inf /home/sipp/Test_Shobhit/SCRIPTS/ConvConfScripts/UAS_Conv_Conf_RTP_SRTP.csv -t l1 
