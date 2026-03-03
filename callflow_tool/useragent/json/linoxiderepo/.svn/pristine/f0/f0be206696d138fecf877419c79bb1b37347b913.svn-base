import random
import socket
from sipconstants import CRLF

    
def genCNonce():
    random_number = random.randint(0,(2**128)-1)
    hex_number = hex(random_number).lstrip('0x')    
    return hex_number

def randomNumber(num_digits):
    lower = 10**(num_digits-1)
    upper = 10**num_digits - 1
    return random.randint(lower, upper)

def createFromTag():
    return f'F{randomNumber(4)}'

def createToTag():
    return f'T{randomNumber(4)}'

def createCallID():
    return f'{randomNumber(7)}'

def createBranchID():
    return f'z9hG4bK{randomNumber(6)}'

def genRSeq():
    return random.randint(1,(2**32)-1)

def getMyHostIP():    
    return Util.my_ip

def isInErrorResponseCode(respcode):
    if respcode in ['400','401','402','403','404','405','406','407',
                    '408','410','413','414','415','416','420','421',
                    '423','480','481','482','483','484','485','486',
                    '487','488','491','500','501','502','503','504']:
        return True
    else:
        return False

class Util:
    my_ip = ""
    stop_reading_msgBuff = False
    chThread_recvMedia = None
    chThread_sendMedia = None
    clientTimeout = 60
    timeLapseBeforeBye = 3