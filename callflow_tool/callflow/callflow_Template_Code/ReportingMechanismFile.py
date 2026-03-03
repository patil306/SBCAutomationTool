import paramiko
import threading
import json
import helper
import datetime
reasontext = "No reason"
number_of_testcases_passed = 0
def getFileContetn(client):
    sftp = client.open_sftp()
   # stdin, stdout, stderr = client.exec_command("cat /root/useragent/testreport.json")
    while(1):
        try:
            print(sftp.stat('/root/useragent/testreport.json'))
            stdin, stdout, stderr = client.exec_command("cat /root/useragent/testreport.json")
            print('file exists')
            break
        except IOError:
            stdin, stdout, stderr = client.exec_command("cat /root/useragent/testreport.json")
            pass
            #print("TTTTTT")
            #break
        except Exception as e:
            pass
            #print("PPPPP")
            #print(e)

    stdout = stdout.read().decode("utf-8")
    #print("WWW")
    #print(stdout)
    result_dict = json.loads(stdout)
    return result_dict

def monitor(ip):
    global reasontext
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username="root", password="SIPera_123")
    #stdin, stdout, stderr = client.exec_command("awk '{print $1}' %s", TESTREPORT)
    while(1):
        result_dict = getFileContetn(client)
        print("RESULT DICT")
        print(result_dict)
        print(result_dict.get("_TestReport__status"))
        if(result_dict.get("_TestReport__status") == None):
            continue
        elif(result_dict.get("_TestReport__status") == "COMPLETE"):
            #    result = result_dict.get("result")
                result = result_dict.get("_TestReport__result")
                sig_result = result_dict.get("_TestReport__signalingReport")
                med_result = result_dict.get("_TestReport__mediaReport")
                print(result)
                stdin, stdout, stderr = client.exec_command("rm -rf /root/useragent/testreport.json")
                client.close()
                if ((sig_result == "PASS" and med_result == "PASS") or (result == "PASS")):
                    #csvstr = result_dict.get("status") + "," + result_dict.get("result") + "," + result_dict.get("reason_code") + "\n"
                    #with open("testreporting.csv", "a+") as f:
                     #   f.write(csvstr)
                    return "success"
                elif(sig_result == "PASS" and (med_result == "NONE" or med_result == "FAIL")):
                    reasontext = "Media failure"
                    return reasontext
                elif(result == "NONE"):
                    reasontext = result_dict.get("_TestReport__reason")

                    return "testfailed"
                else:
                    reasontext = "Could not find reason"
                    return "testfailed"
                break


    print(result_dict)
    print("Monitoring over in " + ip)
    pass
########################################################
def startMonitoring(mapNodeIp, tid, test_desc, currtemp_id):
    print("startMonitoring")
    resultflag = 1

    for i in mapNodeIp:
        print("mapNodeIp")
        print(mapNodeIp[i][0])
        isResult = monitor(mapNodeIp[i][0])
        if(isResult == "testfailed"):
            print("$$$$")
            print(isResult)
            resultflag = 0
            break
    print("#####")
    print(isResult)
    print(resultflag)
    if(resultflag == 1):#csvstr = result_dict.get("status") + "," + result_dict.get("result") + "," + result_dict.get("reason_code") + "\n"
        print("*****")
        print(tid)
        helper.Util._testcases_passed += 1
        date = str(datetime.date.today())
        csvstr = tid+", "+test_desc+", completed, pass, no_code, "+date+", "+currtemp_id+"\n"
        with open("/home/pgokhe/venv/callflow/callflow_Template_Code/testreporting.csv", "a+") as f:
            f.write(csvstr)
    elif(resultflag == 0):
        reason_code = reasontext
        date = str(datetime.date.today())
        csvstr = tid+", "+test_desc+", completed, fail, " + reason_code+", "+date+", "+currtemp_id+"\n"
        with open("/home/pgokhe/venv/callflow/callflow_Template_Code/testreporting.csv", "a+") as f:
            f.write(csvstr)
    pass