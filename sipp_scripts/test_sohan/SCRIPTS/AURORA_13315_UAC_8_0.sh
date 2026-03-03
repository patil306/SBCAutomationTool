#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_13315_UAC_issue_reproduce.xml 10.133.48.83:5061 -i 10.133.39.159 -inf test420.csv -p 5093 -t l1  -aa -trace_msg  -trace_err -m 1
/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_13315_UAC_200OK_WITHOUT_SDP.xml 10.133.48.83:5061 -i 10.133.39.159 -inf test420.csv -p 5093 -t l1  -aa -trace_msg  -trace_err -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_13315_UAC_183_with_nonzero_video_and_200OK_with_zero.xml 10.133.48.83:5061 -i 10.133.39.159 -inf test420.csv -p 5093 -t l1  -aa -trace_msg  -trace_err -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_13315_UAC_183_with_audio_200Ok_with_audio_video.xml 10.133.48.283:5061 -i 10.133.39.159 -inf test420.csv -p 5093 -t l1  -aa -trace_msg  -trace_err -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_13315_UAC_NULL_INVITE.xml 10.133.48.83:5061 -i 10.133.39.159 -inf test420.csv -p 5093 -t l1  -aa -trace_msg  -trace_err -m 1
mv ../XML/AURORA_13315_UAC*.log ../SIPP_LOGS/
