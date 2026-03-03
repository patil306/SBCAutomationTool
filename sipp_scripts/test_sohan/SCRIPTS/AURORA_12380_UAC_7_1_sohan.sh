#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_12380_UAC.xml 10.133.48.151:5060 -i 10.133.39.159 -inf test420.csv -p 6001 -t t2  -aa -trace_msg  -trace_err -m 1
/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_12380_UAS.xml 10.133.48.151:5060 -i 10.133.39.159 -inf test420.csv -p 6001 -t t2  -aa -trace_msg  -trace_err -m 1
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_12380_UAS.xml 10.133.48.151:5060 -i 10.133.39.159 -inf test420.csv -p 6001   -aa -trace_msg  -trace_err -m 1
mv ../XML/AURORA_12380_UAC*.log ../SIPP_LOGS/
