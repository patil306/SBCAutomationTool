/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_15034_UAS_Transfer_Target.xml 192.168.55.75:5060 -i 192.168.5.12 -inf Transfer_Target.csv -p 6020 -t t1  -m 1 -aa -trace_msg  -trace_err
mv ../XML/AURORA_15034_UAS_Transfer_Target*.log ../SIPP_LOGS/
