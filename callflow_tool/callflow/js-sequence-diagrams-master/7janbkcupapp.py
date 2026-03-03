from flask import render_template, Flask, request
import  re
import json
import paramiko
PROXYDEVICES = ["SBC", "SM", "CM", "IPO"]
KEYLIST = ["method", "direction","callid" ,"hassdp","targetnodenames","nextnode", "INS_HDR", "REP_HDR", "REM_HDR", "REP_REQURI", "REM_REQURIPARAM"]
app = Flask(__name__, static_folder="/home/pgokhe/venv/callflow/js-sequence-diagrams-master" ,template_folder="/home/pgokhe/venv/callflow/js-sequence-diagrams-master")
#node ounters
EXT_CNT = 0
INT_CNT = 0
RW_CNT = 0
CALLFLOW = ""

##VM details
EXT_VM_IP = "10.133.48.63"
INT_VM_IP = "10.133.48.64"
RW_VM_IP =  "10.133.48.63"
RW2_VM_IP = "10.133.48.64"
REMOTEJSONPATH = "/root/useragent/json/"            #this will be common on all the n
EXTJSON = "ext.json"
INTJSON = "int.json"
RWJSON = "rw.json"
RW2JSON = "rw2.json"
################################################################################################################
def generateCallid():
        pass

def copyJsonToVM(filename, hostname):        #type can be ext, int,rw
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname= hostname, username ="root", password = "SIPera_123")
        ftp_client = ssh_client.open_sftp()
        ftp_client.put(filename, REMOTEJSONPATH+filename)
        ftp_client.close()

def find_count_clients(callflow_str):
        client_list = []
        for line in callflow_str.splitlines():
                parts = re.split(":", line)
                parts = re.split("->", parts[0])
                #print(parts)
                for i in parts:
                        if i not in PROXYDEVICES + client_list:
                                client_list.append(i)

        return (client_list, len(client_list))
        pass
##########################################################
def FindsLineRequiredforNode(NodeName, callflow_str):
        global CALLFLOW
        CALLFLOW =  callflow_str
        related_lines = []
        
        for line in callflow_str.splitlines():
                parts = re.split(":", line)     #parts[0] is in format A->B , parts[1] is messege like INVITE,180etc
                flow = re.split("->", parts[0])
                if (NodeName in flow and NodeName not in PROXYDEVICES):
                        related_lines.append(line)

        return  related_lines
        pass

####################################################################
def findTargetNodeNames(nextLines, MyNodeName, MyMethod):
        print("findTargetNodeName")
        print(nextLines)
        print(MyNodeName)
        print(MyMethod)
        targets = []            #this is targetNode that is target phone type
        nextNode = []           #this should always be SBC/SM/IPO
        for line in nextLines:
                if ((MyMethod in line) and (MyNodeName not in line)):
                        print("the target is hidden in the ", line)
                        parts = re.split(":", line)
                        nodes = re.split("->", parts[0])
                        if(nodes[0] in PROXYDEVICES):
                                if(nodes[1] not in PROXYDEVICES):
                                        targets.append(nodes[1])
                                nextNode.append(nodes[0])
        
        return targets, nextNode
                                
        pass
####################################################
def FindTargetName(MyNodeName, myMethod, current_line):
        print("callflow is")
        localcallflow = CALLFLOW.splitlines()
        print(localcallflow)

        if(current_line in localcallflow):
                index = localcallflow.index(current_line)
                desiredTargetLines = localcallflow[index+1:]
                #print("DESIRED TARGET MAY BE FOUND IN ")
                #print(desiredTargetLines)
                targetnames, nextnodenames = findTargetNodeNames(desiredTargetLines, MyNodeName, myMethod)
                return targetnames, nextnodenames
                pass
        pass
#################################################
def GetInfo(data, line, NodeName):
        print("THE LINE currently being proccessed for getting data is :" + line)
        parts = re.split(":", line)
        met = re.split("\[", parts[1])
        data["method"] = met[0]
        parts = re.split("->", line)
        if(parts[0] == NodeName):
                data["direction"] = "send"
        else:
                data["direction"] = "recv"
        
        ###new edit 
        if(data["direction"] == "send"):
                targetnames, nextnodenames = FindTargetName(MyNodeName = NodeName, myMethod = data["method"], current_line = line)
                data["targetnodenames"] = targetnames
                if(targetnames[0] == "a_rw" or targetnames[0] == "A_rw"):
                        data["targetextn"] = "9001"
                elif (targetnames[0] == "b_rw" or targetnames[0] == "B_rw"):
                        data["targetextn"] = "9002"
                data["nextnode"] = nextnodenames[0]
                
        ###new edit ends
        start = line.find("[") + 1
        end   = line.find("]")
        if(start and end):
                parts = re.split(",", line[start:end])
                x = {}
                y = {}
                z = {}
                INSHDR = []
                REPHDR = []
                REMHDR = []
                INSSDPMLINE = []
                INSSDPSESSATTR = []
                INSREQURIPARAM = []
                REMREQURIPARAM = []
                for i in parts:
                        i = i.strip()
                      #  print(i)
                        if ("REP_REQURI:" in i):
                                s = i.find('\"') + 1
                                e = i.rfind('\"')
                                if(s and e):
                                        data["REP_REQURI"] = i[s:e]
                        if("INS_HDR" in i):
                                print("HEER")
                                if (i[3] == "_"):
                                        print("ALSO HEER")
                                        k = i
                                        s = k.find('\"') + 1
                                        e = k.rfind('\"')
                                        print(s)
                                        print(e)
                                        print(k)
                                        if (s and e):
                                                print(k)

                                                INSHDR.append(k[s:e])
                                        # print(x)
                                pass
                        if ("REP_HDR" in i):
                                print("REP_HDR")
                                if (i[3] == "_"):
                                        print("ALSO REP_HDR")
                                        k = i
                                        s = k.find('\"') + 1
                                        e = k.rfind('\"')
                                        print(s)
                                        print(e)
                                        print(k)
                                        if (s and e):
                                                print(k)

                                                REPHDR.append(k[s:e])
                                        # print(x)
                                pass
                        if ("REM_HDR" in i):
                                print("REM_HDR")
                                if (i[3] == "_"):
                                        print("ALSO REM_HDR")
                                        k = i
                                        s = k.find('\"') + 1
                                        e = k.rfind('\"')
                                        print(s)
                                        print(e)
                                        print(k)
                                        if (s and e):
                                                print(k)

                                                REMHDR.append(k[s:e])
                                        # print(x)
                                pass
                        if("INS_REQURIPARAM"in i):
                                print("INS_REQURIPARAM")
                                if(i[3] == "_"):
                                        k = i
                                        s = k.find('\"') + 1
                                        e = k.rfind('\"')
                                        if(s and e):
                                                INSREQURIPARAM.append(k[s:e])

                                pass
                        if("REM_REQURIPARAM" in i):
                                print("REM_REQURIPARAM")
                                if (i[3] == "_"):
                                        k = i
                                        s = k.find('\"') + 1
                                        e = k.rfind('\"')
                                        if (s and e):
                                                REMREQURIPARAM.append(k[s:e])
                                pass
                        if("INS_SDPSESSATTR" in i):
                                print("INS_SDPSESSATTR")
                                if (i[3] == "_"):
                                        k = i
                                        s = k.find('\"') + 1
                                        e = k.rfind('\"')
                                        if (s and e):
                                                INSSDPSESSATTR.append(k[s:e])
                                pass

                        if("INS_SDMPLINE" in i):
                                if (i[3] == "_"):
                                        k = i[4:]
                                        s = k.find('\"') + 1
                                        e = k.rfind('\"')
                                        if (s and e):
                                                INSSDPMLINE.append(k[s:e])
                                              #  print(y)
                                                
                                pass

                        print("DSDS")
                        print(x)
                        data["INS_HDR"] = INSHDR
                        data["REP_HDR"] = REPHDR
                        data["REM_HDR"] = REMHDR
                        data["INS_SDPMLINE"] = INSSDPMLINE
                        data["INS_SDPSESSATTR"] = INSSDPSESSATTR
                        data["INS_REQURIPARAM"] = INSREQURIPARAM
                        data["REM_REQURIPARAM"] = REMREQURIPARAM
                        pass
        return  data
        pass
##################################################
def MakeDictionaryWithInfo(NodeName, related_lines):
        seq_count = 0
        Dict = {}
        global  EXT_CNT, INT_CNT, RW_CNT
        print("MakeDictionaryWithInfo")
        print("LINES RELATED TO " + NodeName + " ARE " + str(related_lines))
        if(NodeName[-3:] == "ext" or NodeName[-3:] == "EXT"):
                Dict["type"] = "EXT"
                EXT_CNT = EXT_CNT + 1
                Dict["extn"] = "700"+str(EXT_CNT)
                Dict["domain"] = "at&t.com"
        elif (NodeName[-3:] == "INT" or NodeName[-3:] == "INT"):
                Dict["type"] = "INT"
                INT_CNT = INT_CNT + 1
                Dict["extn"] = "800" + str(INT_CNT)
                Dict["domain"] = "avaya.com"
        if (NodeName[-2:] == "rw" or NodeName[-3:] == "RW"):
                Dict["type"] = "RW"
                RW_CNT = RW_CNT + 1
                Dict["extn"] = "900" + str(RW_CNT)
                Dict["domain"] = "avaya.com"

        for line in related_lines:
                data_for_node = {key: None for key in KEYLIST}
                data_for_node = GetInfo(data_for_node, line, NodeName)
                Dict[seq_count] = data_for_node
                seq_count = seq_count + 1
        print(Dict)
        return Dict
        #print(Dict)
            
        pass
###################################################
def processNode(NodeName, callflow_str):
        lines_related_to_node = FindsLineRequiredforNode(NodeName, callflow_str)

        if (len(lines_related_to_node) > 0):
                nodeDict = MakeDictionaryWithInfo(NodeName, lines_related_to_node)
                return nodeDict
                pass
        else:
                print("Node "+ NodeName +" has no related flow in diagram" )
        pass
#########################################################
def processCallflow(callflow_str):
        clients, number_of_clients = find_count_clients(callflow_str)
        NodeInfo = {}
        global EXT_CNT, INT_CNT, RW_CNT
        EXT_CNT = 0
        INT_CNT = 0
        RW_CNT = 0
        print("NUMBER OF NODES is "+ str(number_of_clients))
        print(clients)
        for i in clients:
                NodeInfo[i] = processNode(i, callflow_str)
                if("_ext" in i):  #write to to ext.json
                        if (EXT_CNT == 1):
                                with open('ext.json', 'w') as f:
                                        json.dump({i:NodeInfo[i]}, f, indent=4)
                                #copyJsonToVM("ext.json", EXT_VM_IP)
                        else:
                                with open('ext2.json', 'w') as f:
                                        json.dump({i:NodeInfo[i]}, f, indent=4)
                                #copyJsonToVM("ext2.json", EXT2_VM_IP)
                        pass
                elif("_int" in i):  #write to int.json
                        if(INT_CNT == 1):
                                with open('int.json', 'w') as f:
                                        json.dump({i:NodeInfo[i]}, f, indent=4)
                       # copyJsonToVM("int.json", INT_VM_IP)
                        else:
                                with open('int2.json', 'w') as f:
                                        json.dump({i: NodeInfo[i]}, f, indent=4)
                        # copyJsonToVM("int2.json", INT2_VM_IP)

                        pass
                elif("_rw" in i):   #write to rw.json

                        if(RW_CNT == 1):
                                with open('rw.json', 'w') as f:
                                        json.dump({i:NodeInfo[i]}, f, indent=4)
                                copyJsonToVM("rw.json", RW_VM_IP)
                        else:
                                with open('rw2.json', 'w') as f:
                                        json.dump({i:NodeInfo[i]}, f, indent=4)
                                copyJsonToVM("rw2.json", RW2_VM_IP)
                        pass

        
        print("NODE INFO is")
        print(json.dumps(NodeInfo, indent=4))
        

@app.route('/', methods=["GET", "POST"])
def button():
        name = request.get_json()
        print(type(name))
        if(name):
                #copyJsonToVM(hostname="10.133.48.63")
                processCallflow(name['ajson'])
        return render_template("index_js.html")

if __name__ == '__main__':
	app.run(host='10.133.99.221', port=7000)

