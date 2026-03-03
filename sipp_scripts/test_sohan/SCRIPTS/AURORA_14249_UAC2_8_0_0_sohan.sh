/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14249_UAC2_backup_17_08_2018.xml 10.133.48.87:5060 -i 10.133.39.159 -inf test420.csv -p 5097 -t t1  -aa -trace_msg  -trace_err -m 1 -rp 2000
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14249_UAC2_PRACK_22_08_2018.xml 10.133.48.238:5061 -i 10.133.39.159 -inf test420.csv -p 5091 -t l1  -aa -trace_msg  -trace_err -m 1 -rp 2000
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14249_UAC2_PRACK_20_08_2018_test4_crucible_comment.xml 10.133.48.238:5061 -i 10.133.39.159 -inf test420.csv -p 5091 -t l1  -aa -trace_msg  -trace_err -m 1 -rp 2000
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14249_UAC2_test_case5_crucible.xml 10.133.48.238:5061 -i 10.133.39.159 -inf test420.csv -p 5091 -t l1  -aa -trace_msg  -trace_err -m 1 -rp 2000
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14249_UAC2_test_case6_crucible.xml 10.133.48.238:5061 -i 10.133.39.159 -inf test420.csv -p 5091 -t l1  -aa -trace_msg  -trace_err -m 1 -rp 2000
#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14249_UAC2_test_case7_reinvite_sdp.xml 10.133.48.238:5061 -i 10.133.39.159 -inf test420.csv -p 5091 -t l1  -aa -trace_msg  -trace_err -m 1 -rp 2000
mv ../XML/AURORA_14249_UAC*.log ../SIPP_LOGS/
