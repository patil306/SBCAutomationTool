from flask import render_template, Flask, request
import  re
import json

PROXYDEVICES = ["SBC", "SM", "CM", "IPO"]
KEYLIST = ["method", "direction", "hassdp", "RequestUri", "modifyheader", "modifycontent", "HeaderParam", "targetnodenames"]
app = Flask(__name__, static_folder="C:\\Users\ydeshpande\Desktop\FILES\call flow\js-sequence-diagrams\js-sequence-diagrams-master" ,template_folder="C:\\Users\ydeshpande\Desktop\FILES\call flow\js-sequence-diagrams\js-sequence-diagrams-master")

EXT_CNT = 0
INT_CNT = 0
RW_CNT = 0
CALLFLOW = ""
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
        targets = []
        for line in nextLines:
                if ((MyMethod in line) and (MyNodeName not in line)):
                        print("the target is hidden in the ", line)
                        parts = re.split(":", line)
                        nodes = re.split("->", parts[0])
                        if(nodes[0] in PROXYDEVICES):
                                targets.append(nodes[1])
        
        return targets
                                
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
                targetnames = findTargetNodeNames(desiredTargetLines, MyNodeName, myMethod)
                return targetnames
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
                targetnames = FindTargetName(MyNodeName = NodeName, myMethod = data["method"], current_line = line)
                data["targetnodenames"] = targetnames
                
        ###new edit ends
        start = line.find("[") + 1
        end   = line.find("]")
        if(start and end):
                parts = re.split(",", line[start:end])
                x = {}
                y = {}
                z = {}
                for i in parts:
                        i = i.strip()
                      #  print(i)
                        if ("RURI:" in i):
                                s = i.find('\"') + 1
                                e = i.rfind('\"')
                                if(s and e):
                                        data["RequestUri"] = i[s:e]

                        if("HDR" in i):
                                print("HEER")
                                if(i[3] == "_"):
                                        print("ALSO HEER")
                                        k = i[4:]
                                        s = k.find('\"') + 1
                                        e = k.rfind('\"')
                                        print(s)
                                        print(e)
                                        print(k)
                                        if (s and e):
                                                print(k)

                                                x[k[:s-2]] = k[s:e]
                                               # print(x)
                                pass
                        if("SDP" in i):
                                if (i[3] == "_"):
                                        k = i[4:]
                                        s = k.find('\"') + 1
                                        e = k.rfind('\"')
                                        if (s and e):
                                                y[k[:s - 2]] = k[s:e]
                                              #  print(y)
                                                
                                pass
                        if("HDRPARAM" in i):
                                if (i[3] == "P"):
                                        k = i[9:]
                                        s = k.find('\"') + 1
                                        e = k.rfind('\"')
                                        if (s and e):
                                                z[k[:s - 2]] = z[s:e]
                                pass
                        print("DSDS")
                        print(x)
                        data["modifyheader"] = x
                        data["modifycontent"] = y
                        data["HeaderParam"] = z
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
                INT_CN1
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
        
        print("NODE INFO is")
        print(json.dumps(NodeInfo, indent=4))
        

@app.route('/', methods=["GET", "POST"])
def button():
        name = request.get_json()
        print(type(name))
        if(name):
                processCallflow(name['ajson'])
        return render_template("index_js.html")

