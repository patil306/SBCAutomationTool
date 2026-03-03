#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_13315_UAS_issue_reproduce.xml 192.168.6.246 -i 192.168.6.5 -inf test420.csv -p 5091 -t l1  -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_13315_UAS_200OK_WITHOUT_SDP.xml 192.168.6.246 -i 192.168.6.5 -inf test420.csv -p 5091 -t l1  -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_13315_UAS_183_with_nonzero_video_and_200OK_with_zero.xml 192.168.6.246 -i 192.168.6.5 -inf test420.csv -p 5091 -t l1  -m 1 -aa -trace_msg  -trace_err
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_13315_UAS_183_with_audio_200Ok_with_audio_video.xml 192.168.6.246 -i 192.168.6.5 -inf test420.csv -p 5091 -t l1  -m 1 -aa -trace_msg  -trace_err
/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_13315_UAS_NULL_INVITE.xml 192.168.6.246 -i 192.168.6.5 -inf test420.csv -p 5091 -t l1  -m 1 -aa -trace_msg  -trace_err
mv ../XML/AURORA_13315_UAS*.log ../SIPP_LOGS/
