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
    return f'F_{randomNumber(4)}'

def createToTag():
    return f'T_{randomNumber(4)}'

def createCallID():
    return f'{randomNumber(7)}'

def createBranchID():
    return f'z9hG4bK{randomNumber(6)}'

def genRSeq():
    return random.randint(1,(2**32)-1)



class Util:
    _hostIP = ""
    _stopTraffic = True

def getMyHostIP():
    return Util._hostIP
def stopTraffic():
    Util._stopTraffic = True
def isStopTraffic():
    return True if Util._stopTraffic else False
def isTrafficOn():
    return False if Util._stopTraffic else True



