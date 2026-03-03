PROXYDEVICES = ["SBC", "SM", "CM", "IPO"]
USERAGENTS = [ "A_ext", "B_ext", "C_ext", "A_rw", "B_rw", "C_rw","A_int", "B_int", "C_int", "A_EXT", "B_EXT", "C_EXT", "A_RW", "B_RW", "C_RW","A_INT", "B_INT", "C_INT","A_ext", "B_ext", "C_ext", "A_rw", "B_rw", "C_rw","A_int", "B_int", "C_int", "a_ext", "b_ext", "c_ext", "a_rw", "b_rw", "c_rw","a_int", "b_int", "c_int"]

KEYLIST = ["event", "method","direction","dialogid" ,"hascontent","hascontentchanged","targetnodenames","mediadirection","nextnode", "INS_HDR", "REP_HDR", "REM_HDR", "REP_REQURI", "REM_REQURIPARAM", "INS_SDPMLINE", "INS_SDPSESSATTR", "INS_SDPAUDIOCODEC"]
#node ounters
EXT_CNT = 0
INT_CNT = 0
RW_CNT = 0
CALLFLOW = ""

##VM details
EXT1_VM_IP = "10.133.43.54"
EXT2_VM_IP = "10.133.43.55"
INT1_VM_IP = "10.133.43.56"
INT2_VM_IP = "10.133.43.57"
RW1_VM_IP = "10.133.43.51"
RW2_VM_IP = "10.133.43.52"
RW3_VM_IP = "10.133.43.53"
CONTROLLERIP = "10.133.99.221"
CALLFLOWJSONPATH = "/root/useragent/json/"            #this will be common on all the vm
CLIENTPATH = "/root/useragent/json/linoxiderepo/useragent.py"
CONFIGJSONPATHMASTER = "/root/JSON/SBC/"
CONFIGJSONPATHTMP = "/root/JSON/TMP/"
SBCRWINTERFACE = "10.133.60.65"
SBCEXTINTERFACE = "10.133.60.69"
SBCINTINTERFACE = ""
SMIP = "192.168.1.80"
IPOIP = "x.y.z.w"
RW_USER_1 = "4441000024"
RW_USER_2 = "4441000025"
RW_USER_3 = "4441000026"
INT_USER_1 = "4441000024"
INT_USER_2 = "4441000025"
INT_USER_3 = "4441000026"
TRK_USER_1 = "8001"
TRK_USER_2 = "8002"
TRK_USER_3 = "8003"
GLOBALDOMAIN = "sbcsv.com"
