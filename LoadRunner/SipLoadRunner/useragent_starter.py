import time
import sys
import subprocess
myIp = sys.argv[1]
num_hours = sys.argv[2]

cmd =  "python3 useragent.py -i "+ myIp +" -r 10.133.39.154 -t -d bsnl.com -p 5060 -s 3600 --clr 4002 --cle 4001 --uac"
for i in range(int(num_hours)):
    start_tool = subprocess.run(["cat"],stdout=subprocess.PIPE, text=True, input="Hello from the other side")
    time.sleep(3780)
    os.s

print("FROM OTHER script")
print(start_tool.stdout)
