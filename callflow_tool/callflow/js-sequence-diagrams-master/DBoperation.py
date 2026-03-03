import psycopg2
import os
KEYLIST = ["mediarules.json", "sessionpolicies.json", "serverinterworking.json", "sipserverprofiles.json", "signalingrules.json", "featurecontrol.json", "topologyhiding.json"]

def insertinConfigDB(modifiedconfigflies):
    conn = psycopg2.connect(
        database="test",
        user='postgres',
        password='SIPera_123',
        host='localhost',
        port='5432'
    )
    cursor = conn.cursor()
    content = {key: None for key in KEYLIST}
    modifiedconfigflies = os.listdir("/root/JSON/TMP/")
    print(modifiedconfigflies)
    #id = "select count(*) from SBCCONFIG"
    for i in modifiedconfigflies:
        with open("/root/JSON/TMP/"+i, "r") as f:
            content[i.lower()] = f.read()
    query = "insert into SBCCONFIG( mediarules, sessionpolicies, serverinterworking, sipserverprofiles, signalingrules, featurecontrol, topologyhiding) values (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    data = (content["mediarules.json"], content["sessionpolicies.json"], content["serverinterworking.json"], content["sipserverprofiles.json"], content["signalingrules.json"], content["featurecontrol.json"], content["topologyhiding.json"])
    print(cursor.execute(query, data))
    print("SUCESSFULLY inserted configuration in database")
    id_of_new_row = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    print("ID of NEW ROW " + str(id_of_new_row))
    return id_of_new_row        #return comfigid
    pass

def insertinDB(callflow_str, testdesc):
  #  global TID
    modifiedconfigfiles = os.listdir("/root/JSON/TMP/")
    if (modifiedconfigfiles == []):
        sbcconfigid = -1
        cmconfigid = -1
        ipoconfigid = -1
    else:
        sbcconfigid = insertinConfigDB(modifiedconfigfiles)
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

    query = "insert into testcases (description, callflow, sbcconfigid, cmconfigid, ipoconfigid) values (%s, %s, %s, %s, %s)"
    data = (description, callflow_str, sbcconfigid, cmconfigid, ipoconfigid)
    print("SUCCESSFULLY REACHED DB ends")
    cursor.execute(query, data)
    conn.commit()
    cursor.close()
    conn.close()
  #  TID = TID + 1
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