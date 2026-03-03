import subprocess
import os
import json
import time
import rootSSH
import paramiko

def setEnv():
        os.environ['GOVC_URL'] = 'insntdvitfarm.apac.avaya.com:443'
        os.environ['GOVC_USERNAME'] = 'GLOBAL\sbcedvit'
        os.environ['GOVC_PASSWORD'] = 'ApQtFeJD82db8wpHFUTpu2DMHDsXGTjF'
        os.environ['GOVC_INSECURE'] = 'true'
        os.environ['GOVC_DATACENTER'] = 'Pune_Shared'
        os.environ['GOVC_DATASTORE'] = 'SharedVol-VxFlex2-01'
        os.environ['GOVC_RESOURCE_POOL'] = 'DEV_Test_Envs'
        temp=subprocess.Popen('govc about',universal_newlines=True, shell=True, stdout = subprocess.PIPE).communicate()
        output = str(temp)
        print(output)


def deployVM(name,network,ip,gateway,smask):

        print("deployVM " +name)
        print("importing spec file...")
        cmd = 'govc import.spec Ubuntu_20.04.2_VM_LinuxVMImages.ovf >' +name+ '.json'
        temp=subprocess.Popen(cmd ,universal_newlines=True, shell=True, stdout = subprocess.PIPE).communicate()
        print("imported successfully!")

        print("configuring spec file...")
        filename=name+'.json'
        with open(filename, 'r+') as f:
                data = json.load(f)

                for item in data['NetworkMapping']:
                        item['Network'] = network

                data['Name'] = name # <--- add `name` value.
                data['WaitForIP'] = True
                f.seek(0)        # <--- should reset file position to the beginning.
                json.dump(data, f, indent=4)
                f.truncate()     # remove remaining part

        print("configured successfully!")

        print("deploying OVF template...")
        cmd = 'govc import.ovf -options=' +name+ '.json  Ubuntu_20.04.2_VM_LinuxVMImages.ovf'
        print(cmd)
        temp=subprocess.Popen(cmd ,universal_newlines=True, shell=True, stdout = subprocess.PIPE).communicate()

        print("deployed successfully!")

        print("assigning IP address...")
        cmd='govc vm.customize -ip ' + ip + ' -gateway '+gateway+ ' -netmask ' +smask+ ' -vm '+name
        temp=subprocess.Popen(cmd, universal_newlines=True, shell=True, stdout = subprocess.PIPE).communicate()
        print("Assigned IP successfully!")

        cmd='govc vm.power -on '+name
        temp=subprocess.Popen(cmd, universal_newlines=True, shell=True, stdout = subprocess.PIPE).communicate()
        print("powered on vm!")

        time.sleep(300)
        print("################ " + name +"################################")
        try:
            cmd = "chmod -R 777 /root"
            copyuseragenttoroot(ip, cmd)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, username='ubuntu', password='ubuntu')
            scp = ssh.open_sftp()
            scp.put('useragent.tar', '/root/useragent.tar')
            # Close the SCP client
            scp.close()
            ssh.close()
            print("useragent code copied in try " + name)
            pass
        except:
            cmd = "chmod -R 777 /root"
            copyuseragenttoroot(ip, cmd)
            # cmd='scp -r useragent ubuntu@' + ip +':/root/'
            # temp=subprocess.Popen(cmd, universal_newlines=True, shell=True, stdout = subprocess.PIPE).communicate()
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, username='ubuntu', password='ubuntu')
            scp = ssh.open_sftp()
            scp.put('useragent.tar', '/root/useragent.tar')
            # Close the SCP client
            scp.close()
            # Close the SSH client
            ssh.close()
            print("useragent code copied in except " + name)

            pass
def copyuseragenttoroot(ip, cmd):
        time.sleep(20)
        sshcli = rootSSH.SSH()
        sshcli.run_sudo_command("ubuntu", "ubuntu", ip, cmd)
        pass

def userinput():
        name = input("Enter a name of vm: ")
        network = input("Enter a network: ")
        ip = input("Enter an IP: ")
        gateway = input("Gateway: ")
        smask = input("Subnet mask: ")

        return name, network, ip, gateway,smask
        #deployVM(name,network,ip,gateway,smask)


import threading
def main():
        print("Setting GOVC environment variables...")
        setEnv()

        #internal vm1
        print("\n Enter details to deploy INTERNAL VM 1")
        name, network, ip, gateway,smask = userinput()
        t1 = threading.Thread(target=deployVM, args=(name, network, ip, gateway,smask,))

        #internal vm2
        #######################################################################
        print("\n Enter details to deploy INTERNAL VM 2")
        name, network, ip, gateway,smask = userinput()
        t2 = threading.Thread(target=deployVM, args=(name, network, ip, gateway,smask,))

        #external vm1
        ########################################################################
        print("\n Enter details to deploy EXTERNAL VM 1")
        name, network, ip, gateway,smask = userinput()
        t3 = threading.Thread(target=deployVM, args=(name, network, ip, gateway,smask,))

        #external vm2
        #######################################################################
        print("\n Enter details to deploy EXTERNAL VM 2")
        name, network, ip, gateway,smask = userinput()
        t4 = threading.Thread(target=deployVM, args=(name, network, ip, gateway,smask,))

        #remote worker vm1
        #######################################################################
        print("\n Enter details to deploy REMOTE WORKER VM 1")
        name, network, ip, gateway,smask = userinput()
        t5 = threading.Thread(target=deployVM, args=(name, network, ip, gateway,smask,))

        #remote worker vm2
        #######################################################################
        print("\n Enter details to deploy REMOTE WORKER VM 2")
        name, network, ip, gateway,smask = userinput()
        t6 = threading.Thread(target=deployVM, args=(name, network, ip, gateway,smask,))

        #######################################################################
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
main()

