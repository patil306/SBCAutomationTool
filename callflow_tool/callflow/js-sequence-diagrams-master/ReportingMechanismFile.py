import paramiko
import threading
def monitor(ip):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username="root", password="SIPera_123")
    #stdin, stdout, stderr = client.exec_command("awk '{print $1}' %s", TESTREPORT)
    stdin, stdout, stderr = client.exec_command("ls -lrt")
    client.close()
    print("Monitoring over in " + ip)
    pass
########################################################
def startMonitoring(mapNodeIp):
    threads =[]
    for i in mapNodeIp:
        th = threading.Thread(target=monitor, args=(mapNodeIp[i],))
        th.start()
        threads.append(th)
    for i in threads:
        i.join()
    pass