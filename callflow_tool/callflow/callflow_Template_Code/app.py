from flask import render_template, Flask, request, jsonify, redirect
import  re
import json
import psycopg2
import paramiko
import random
import time
import os
import threading
import requests
import sys
import helper
import DBoperation
from ServiceExecutor import ConfigApiExecutor
#import config
from flask_cors import CORS
import importlib.util
spec = importlib.util.spec_from_file_location("config", sys.argv[1])
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)
config = foo

app = Flask(__name__, static_folder="/home/pgokhe/venv/callflow/callflow_Template_Code")
CORS(app)

curr_tempid = -1

def retrivetestcaseids(templateid):
    query = "select testidlist from templates where id = "+templateid+";"
    conn = psycopg2.connect(
        database="test",
        user='postgres',
        password='SIPera_123',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()
    cursor.execute(query)
    arr = cursor.fetchone()
    cursor.close()
    conn.close()
    return arr[0]
    pass

def retrivetestcasedescs(testcaseids):
    conn = psycopg2.connect(
        database="test",
        user='postgres',
        password='SIPera_123',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()
    arr = []
    for i in testcaseids:
        query = "select description from testcases where id = " + str(i) + ";"
        cursor.execute(query)
        arr.append(cursor.fetchone()[0])

        pass
    cursor.close()
    conn.close()
    return arr
    pass


def gettemplatesValuesFromDB():
    conn = psycopg2.connect(
        database="test",
        user='postgres',
        password='SIPera_123',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()
    query = "select id, name from templates;"
    cursor.execute(query)
    #print(cursor.fetchall())
    arr = cursor.fetchall()
    cursor.close()
    conn.close()
    for i in arr:
        arr[arr.index(i)] = '   '.join(map(str, i))
    print(arr)
    return arr
    pass
def gettestcasesValuesFromDB():
    conn = psycopg2.connect(
        database="test",
        user='postgres',
        password='SIPera_123',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()
    query = "select id, description from testcases;"
    cursor.execute(query)
    #print(cursor.fetchall())
    arr = cursor.fetchall()
    cursor.close()
    conn.close()
    for i in arr:
        arr[arr.index(i)] = '   '.join(map(str, i))
    print(arr)
    return arr
    pass

@app.route('/retrivecallflow', methods=["GET", "POST"])
def retrivecallflow():
    testid = request.args.get('testid', '')
    conn = psycopg2.connect(
        database="test",
        user='postgres',
        password='SIPera_123',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()
    query = "select callflow from testcases where id = "+ str(testid) + ";"
    cursor.execute(query)
    # print(cursor.fetchall())
    arr = cursor.fetchone()
    #print(arr[0])
    cursor.close()
    conn.close()
    print(query)
    #return redirect("10.133.99.221:7000")
    return jsonify({"res": arr[0]})


def doConfigureSBC(configdetails):
    if(configdetails[1] != None):
        content = configdetails[1]
        with open("/root/JSON/TMP/MediaRules.json", "w+") as f:
            f.write(content)
        pass
    if (configdetails[2] != None):
        content = configdetails[2]
        with open("/root/JSON/TMP/sessionpolicies.json", "w+") as f:
            f.write(content)
        pass
    if (configdetails[3] != None):
        content = configdetails[3]
        with open("/root/JSON/TMP/serverinterworking.json", "w+") as f:
            f.write(content)
        pass
    if (configdetails[4] != None):
        content = configdetails[4]
        with open("/root/JSON/TMP/sipserverprofiles.json", "w+") as f:
            f.write(content)
        pass
    if (configdetails[5] != None):
        content = configdetails[5]
        with open("/root/JSON/TMP/signalingrules.json", "w+") as f:
            f.write(content)

    print("Configuring sbc based on /root/JSON/TMP directory")
    arr = os.listdir("/root/JSON/TMP/")
    if (arr == []):
        print("no need to configure tmp directory is empty")
    else:
        config_api_exe = ConfigApiExecutor()
        result = config_api_exe.execute("/root/JSON/TMP/")
        if (result == 1):
            print("CONFIGURATION SUCCESSFUL")
        else:
            print("CONFIG failed")

        pass
    pass
def doRollbackSBC():
    print("ROLLING BACK SBC")
    arr = os.listdir("/root/JSON/TMP/")
    if (arr == []):
        print("No need to rollbalck as tmp is empty")
    else:
        config_api_exe = ConfigApiExecutor()
        result = config_api_exe.execute("/root/JSON/SBC/")
        if (result == 1):
            print("ROLLING BACK successful")
        else:
            print("ROLLBACK FAILED")
    pass
def executeTC(testcaseidlist):
    print("executeTC")
    conn = psycopg2.connect(
        database="test",
        user='postgres',
        password='SIPera_123',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()
    helper.Util._testcases_passed = 0
    helper.Util._totaltestcases = len(testcaseidlist)
    for i in testcaseidlist:
        print("ID is " + i)
        query = "select callflow,sbcconfigid from testcases where id="+i+";"
        test_description = "select description from testcases where id="+i+";"
        cursor.execute(test_description)
        test_description = cursor.fetchone()
        test_description = test_description[0]
        print("ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg")
        print(test_description)
        cursor.execute(query)
        arr = cursor.fetchone()
        #30marchStart
        sbcconfigid = arr[1]
        if(sbcconfigid != -1):
            print("configuring sbc for testcase No."+i)
            retrivedconfigquery = "select * from sbcconfig where id="+str(sbcconfigid)+";"
            cursor.execute(retrivedconfigquery)
            doConfigureSBC(cursor.fetchone())
        #30marchEnd
        helper.button(arr[0], i, test_description, curr_tempid)
        if (sbcconfigid != -1):
            print("rolling back sbc after testcase No." + i)
            doRollbackSBC()
        print(arr[0])
    cursor.close()
    conn.close()

def executeTCwithtempconfig(testcaseidlist):
    print("executeTC")
    conn = psycopg2.connect(
        database="test",
        user='postgres',
        password='SIPera_123',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()
    helper.Util._testcases_passed = 0
    helper.Util._totaltestcases = len(testcaseidlist)
    for i in testcaseidlist:
        print("ID is " + i)
        query = "select callflow,sbcconfigid from testcases where id="+i+";"
        test_description = "select description from testcases where id="+i+";"
        cursor.execute(test_description)
        test_description = cursor.fetchone()
        test_description = test_description[0]
        print("ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg")
        print(test_description)
        cursor.execute(query)
        arr = cursor.fetchone()
        #30marchStart
        sbcconfigid = arr[1]
        if(sbcconfigid != -1):
            print("alredy configured sbc for testcase No."+i)

        #30marchEnd
        helper.button(arr[0], i, test_description)

        print(arr[0])
    cursor.close()
    conn.close()
@app.route('/executetemp', methods=["GET", "POST"])
def executetemp():
    testcaseidlist = request.args.get('testidlist', '')
    testcaseidlist = testcaseidlist.split(",")
    print("SSS")
    print(testcaseidlist)
    if(testcaseidlist != []):
        executeTC(testcaseidlist)
        #th = threading.Thread(target=executeTC, args=(testcaseidlist, ))
        #th.start()
        #th.join()
    #return render_template("help.html")
    return jsonify({"res": "Executing testcases "})
    pass

@app.route('/savetemplate', methods=['GET', 'POST'])
def savetemplate():
    templatename = request.args.get("template_name", '')
    testidlist = request.args.get("testidlist", '')
    if(templatename != "" and testidlist != []):
        DBoperation.insertTemplateToDB(testidlist, templatename)
        return ({"res": "template saved successfully"})

    return ({"res": "Not able to save template"})
    pass

@app.route('/modifytemplate', methods=['GET', 'POST'])
def modifytemplate():
    templateid = request.args.get("template_id", '')
    testidlist = request.args.get("testidlist", '')
    print(testidlist)
    if(templateid != "" and testidlist != []):
        DBoperation.updateTemplateToDB(testidlist, templateid)
        return ({"res": "template updated successfully"})

    return ({"res": "Not able to save template"})
    pass

@app.route('/executeexistingtemp', methods=['GET', 'POST'])
def executeexistingtemp():
    conn = psycopg2.connect(
        database="test",
        user='postgres',
        password='SIPera_123',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()
    templateid = request.args.get('template', '')
    global curr_tempid
    curr_tempid = templateid
    testcasesForTemp = retrivetestcaseids(templateid)
    print(testcasesForTemp)
    testcasesForTemp = testcasesForTemp.split(",")
    query = "select sbcconfigid from templates where id = " + templateid+";"
    cursor.execute(query)
    arr = cursor.fetchone()
    istempConfig = int(arr[0])
    print(istempConfig)
    if(testcasesForTemp != "" and istempConfig == -1):
        th = threading.Thread(target=executeTC, args=(testcasesForTemp,))
        th.start()
        th.join()
    elif(testcasesForTemp != "" and istempConfig != -1):
        print("configuring sbc for Template No." + templateid)
        retrivedconfigquery = "select * from sbcconfig where id=" + str(istempConfig) + ";"
        cursor.execute(retrivedconfigquery)
        doConfigureSBC(cursor.fetchone())
        th = threading.Thread(target=executeTCwithtempconfig, args=(testcasesForTemp,))
        th.start()
        th.join()
        doRollbackSBC()
    else :
        return ({"res": "No testacse is stored in selected template"})

    #return redirect("10.133.99.221:9000", code=200)
    return ({"res":"Started execution of template"})
    pass

##17 april start
@app.route('/modifyexistingtemp', methods=['GET', 'POST'])
def modifyexistingtemp():
    conn = psycopg2.connect(
        database="test",
        user='postgres',
        password='SIPera_123',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()
    templateid = request.args.get('template', '')
    testcasesForTemp = retrivetestcaseids(templateid)
    TestcaseDesciption = retrivetestcasedescs(testcasesForTemp.split(","))
    print(testcasesForTemp)
    d = dict(zip(testcasesForTemp.split(","), TestcaseDesciption))
    print(d)
  #  testcasesForTemp = testcasesForTemp.split(",")
    if(testcasesForTemp == ""):
        return ({"res": "No testacse is stored in selected template"})

    #return redirect("10.133.99.221:9000", code=200)
    cursor.close()
    conn.close()
    print("DDDD")
    print(testcasesForTemp)

    return jsonify({"res":"Completed Modification of template", "TestcasesforTemp": d})
    pass
##17 april ends


def executetemplate(templateID):
    pass
def executetestcase():
    pass

@app.route('/', methods=["GET", "POST"])
def button():
        arr = gettestcasesValuesFromDB()#["1 BASIC CALL A-B", "2 BASIC HOLD", "3 BASIC UNHOLD", "4 LONG HOLD", "5 BLIND TRANSFER", "6 CONSULTATIVE TRANSFER", "7 NG911 BASIC CALL", "8 INVITE With Replaces", "9 DELAYED OFFER"]
        confarr = os.listdir("/root/JSON/SBC/")
       # print(arr)
        temparr = gettemplatesValuesFromDB()
        if(arr != []):
            return render_template("index.html", indices = arr, temps = temparr, configfiles = confarr)
        return render_template("index.html", indices = arr, temps = temparr, configfiles = confarr)


@app.route('/background_process_test2', methods=["GET", "POST"])
def background_process_test2():
        print("Doing SBCE configuration in background")
        master_file_name_token = request.args.get('que_token', '')
        CONFIGJSONPATHMASTER = "/root/JSON/SBC/"
        print(master_file_name_token)
        filename = CONFIGJSONPATHMASTER + master_file_name_token
        with open(filename, 'r') as f:
                main_copy_text = f.read()
        print(main_copy_text)
        return jsonify({"var": main_copy_text})

@app.route("/savejsontotemp", methods=['GET', 'POST'])
def savejsontotemp():
        CONFIGJSONPATHMASTER = "/root/JSON/SBC/"
        CONFIGJSONPATHTMP = "/root/JSON/TMP/"
        newcontent = request.args.get('newconfig_temp', '')
        masterfilename = request.args.get('masterfilename', '')
        tempfilename =  masterfilename
        print(masterfilename)
        filename = CONFIGJSONPATHTMP + tempfilename
        with open(filename, "w") as f:
                f.write(newcontent)
        print(newcontent)
        return jsonify({"response": "OK"})
if __name__ == '__main__':
	app.run(host=config.CONTROLLERIP, port=8000)
