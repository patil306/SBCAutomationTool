#/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14698_UAS.xml 192.168.55.75:5060 -i 192.168.5.12 -inf testdemo.csv -p 5097 -t t1  -m 1 -aa -trace_msg  -trace_err
/home/sipp/sipp.svn/sipp -sf ../XML/AURORA_14698_UAS_test_case_1_media_inst.xml 192.168.55.75:5060 -i 192.168.5.12 -inf testdemo.csv -p 5097 -t t1  -m 1 -aa -trace_msg  -trace_err
mv ../XML/AURORA_14698_UAS*.log ../SIPP_LOGS/
