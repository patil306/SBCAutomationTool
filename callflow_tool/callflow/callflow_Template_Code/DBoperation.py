import psycopg2
import os
KEYLIST = ["mediarules", "sessionpolicies", "serverinterworking", "sipserverprofiles", "signalingrules", "featurecontrol", "topologyhiding"]

def insertinConfigDB(modifiedconfigflies):
    content = {key: None for key in KEYLIST}
    modifiedconfigflies = os.listdir("/root/JSON/TMP/")
    id = "select count(*) from SBCCONFIG"
    for i in modifiedconfigflies:
        with open("/root/JSON/TMP/"+i, "r") as f:
            content[i.lower()] = f.read()
    query = "insert into SBCCONFIG(id, mediarules, sessionpolicies, serverinterworking, sipserverprofiles, signalingrules, featurecontrol, topologyhiding) values (%s, %s, %s, %s, %s, %s, %s, %s)"
    data = (id, content["mediarules"], content["sessionpolicies"], content["serverinterworking"], content["sipserverprofiles"], content["signalingrules"], content["featurecontrol"], content["topologyhiding"])
    return id
    pass


def insertinDB(callflow_str, testdesc):
  #  global TID
    modifiedconfigfiles = os.listdir("/root/JSON/TMP/")
    conn = psycopg2.connect(
        database="test",
        user='postgres',
        password='SIPera_123',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()
    #id = TID#cursor.execute("select count(*) from testcases")
    description = testdesc#"SAMPLE TESTCASE"
    cmconfigid = -1
    ipoconfigid = -1
    if(modifiedconfigfiles == []):
            sbcconfigid = -1
            cmconfigid  = -1
            ipoconfigid = -1
    else:
        sbcconfigid = insertinConfigDB(modifiedconfigfiles)
    query = "insert into testcases (description, callflow, sbcconfigid, cmconfigid, ipoconfigid) values (%s, %s, %s, %s, %s)"
    data = (description, callflow_str, sbcconfigid, cmconfigid, ipoconfigid)
    print("SUCCESSFULLY REACHED DB ends")
    cursor.execute(query, data)
    conn.commit()
    cursor.close()
    conn.close()
  #  TID = TID + 1
    pass

def updateTemplateToDB(testidlist, tempid):
    query = "update templates SET testidlist= %s where id=%s;"
    data = (testidlist, tempid)
    conn = psycopg2.connect(
        database="test",
        user='postgres',
        password='SIPera_123',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()
    cursor.execute(query, data)
    conn.commit()
    cursor.close()
    conn.close()

    pass

def insertTemplateToDB(testidlist, templatename):
    #global TEMPID
    sbcconfigid = -1
    query = "insert into templates (name, testidlist, sbcconfigid) values (%s, %s, %s);"
    data = (templatename, testidlist, sbcconfigid)
    conn = psycopg2.connect(
        database="test",
        user='postgres',
        password='SIPera_123',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()
    cursor.execute(query, data)
    conn.commit()
    cursor.close()
    conn.close()
   # TEMPID = TEMPID + 1
    pass