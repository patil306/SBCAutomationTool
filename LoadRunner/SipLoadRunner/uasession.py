from sdp import SDP
from transport import SignalingSocket
from media import Media
from sipmessage import SipMessage
from sipconstants import SipCallState, SDPState, SipHeaders
import re

class UASession:
    def __init__(self):
        self.__usrName = ""
        self.__callID = None
        self.__localTag = None
        self.__remoteTag = None
        self.__isDlgOwner = False
        self.__remoteTarget = None
        self.__remoteURL = None
        self.__fromHeader = None
        self.__toHeader = None
        self.__localContact = None
        self.__cSeq = 0
        self.__rSeq = 1
        self.__rAck = None
        self.__prevSipMessage = None
        self.__currSipMessage = None  
        self.__msgObjMap = {}      
        self.__sigSocket = None
        self.__mydomain = None
        self.__targetextn = None       
        self.__transport = 'tcp'
        self.__scheme = 'sip'
        self.__routeset = []
        self.__isReliable = False
        self.__isSessionComplete = False
        self.__sessStartTime = 0
        self.__localSDP:SDP = None
        self.__remoteSDP:SDP = None
        self.__sipCallState = SipCallState.IDLE.value
        self.__sdpCallState = SDPState.IDLE.value
        self.__sdpState = SDPState.IDLE.value
        self.__mediaObject = None

    def setLocalSDP(self, sdp):
        self.__localSDP = sdp

    def getLocalSDP(self):
        return self.__localSDP

    def setRemoteSDP(self,sdp):
        self.__remoteSDP = sdp

    def getRemoteSDP(self):
        return self.__remoteSDP

    def setPassword(self, pw):
        self.__password = pw

    def getPassword(self):
        return self.__password
     
    def isKnownDialog(self, callid, frm_tag, to_tag):
        if callid == self.__callID:
            if frm_tag == self.__localTag:
                if to_tag == self.__remoteTag:
                    return True

    def isDialogOwner(self):
        return self.__isDlgOwner

    def setReliable(self,flag):
        self.__isReliable = flag

    def isReliable(self):
        return self.__isReliable

    def setDialogOwner(self,var):
        self.__isDlgOwner = var

    def setLocalTag(self, tag):
        self.__localTag = tag
        
    def getLocalTag(self):
        return self.__localTag
    
    def setRemoteTag(self, tag):
        self.__remoteTag = tag
        
    def getRemoteTag(self):
        return self.__remoteTag
    
    def setCallID(self, callId):
        self.__callID = callId
        
    def getCallID(self):
        return self.__callID
    
    def setRemoteTarget(self, rem_target):
        if rem_target:
            self.__remoteTarget = rem_target
            self.__remoteURL = re.search('<(.*)>',rem_target[0]).group(1)
        
    def getRemoteTarget(self):
        return self.__remoteTarget[0]

    def getRemoteURL(self):
        return self.__remoteURL

    def setFromHeader(self, val):
        self.__fromHeader = val
        
    def getFromHeader(self):
        return self.__fromHeader[0]

    def getFromUserPart(self):
        frm_hdr = self.__fromHeader[0]
        return frm_hdr.split(':',1)[1].split('@',1)[0]
    
    def setToHeader(self, uri):
        self.__toHeader = uri
        
    def getToHeader(self):
        return self.__toHeader[0]

    def getToUserpart(self):
        to_hdr = self.__toHeader[0]
        return to_hdr.split(':',1)[1].split('@',1)[0]
    
    def setLocalContact(self, contact):
        self.__localContact = contact
    
    def getLocalContact(self):
        return self.__localContact

    def setCSeq(self,cseq):
        self.__cSeq = cseq

    def getLastCSeq(self):
        return self.__cSeq

    def setRSeq(self, val):
        self.__rSeq = val

    def getRSeq(self):
        return self.__rSeq
    
    def setRAck(self, rack):
        self.__rAck = rack
        
    def getRAck(self):
        return self.__rAck

    def getURI(self):
        return self.__uri
        
    def setCurSipMessage(self, message):
        self.__prevSipMessage = self.__currSipMessage
        self.__currSipMessage = message
        
    def getCurSipMessage(self) -> SipMessage:
        return self.__currSipMessage
    
    def setPrevSipMessage(self, message):
        self.__prevSipMessage = message
        
    def getPrevSipMessage(self):
        return self.__prevSipMessage 
    
    def addMsgObj(self, msg, msg_obj):
        self.__msgObjMap[msg] = msg_obj   
        
    def getMsgObj(self, evt) -> SipMessage:
        return self.__msgObjMap.get(evt)

    def setSigSocket(self, socket:SignalingSocket):
        self.__sigSocket = socket

    def getSigSocket(self) -> SignalingSocket:
        return self.__sigSocket

    def setUserName(self, extn):
        self.__usrName = extn
        
    def getUserName(self):
        return self.__usrName
    
    def setDomain(self, domain):
        self.__mydomain = domain
        
    def getDomain(self):
        return self.__mydomain
    
    def setTargetExtn(self, extn):
        self.__targetextn = extn
        
    def getTargetExtn(self):
        return self.__targetextn   
    
    def setTransport(self, transport):
        self.__transport = transport
        
    def getTransport(self):
        return self.__transport

    def getScheme(self):
        return self.__scheme
    
    def setScheme(self, scheme):
        self.__scheme = scheme
        
    def setRouteSet(self, rs):
        self.__routeset = rs
        
    def getRouteSet(self):
        return self.__routeset

    def setSessionComplete(self, flag):
        self.__isSessionComplete = flag

    def isSessionComplete(self):
        return self.__isSessionComplete

    def setSessionStartTime(self, time):
        self.__sessStartTime = time

    def getSessionStartTime(self):
        return self.__sessStartTime

    def setSipCallState(self, state: SipCallState):
        self.__sipCallState = state

    def getSipCallState(self):
        return self.__sipCallState

    def getPrevSipCallState(self):
        return self.__prevSipCallState

    def setMediaObject(self, obj: Media):
        self.__mediaObject = obj

    def getMediaObject(self) -> Media:
        return self.__mediaObject

    def setSDPstate(self, state: SDPState):
        if state == SDPState.SDP_SENT.value:
            if self.__sdpState in [SDPState.IDLE.value, SDPState.COMPLETE.value]:
                self.__prevSDPState = self.__sdpState
                self.__sdpState = SDPState.SDP_SENT.value
            elif self.__sdpState == SDPState.SDP_RCVD.value:
                self.__prevSDPState = self.__sdpState
                self.__sdpState = SDPState.COMPLETE.value

        elif state == SDPState.SDP_RCVD.value:
            if self.__sdpState in [SDPState.IDLE.value, SDPState.COMPLETE.value]:
                self.__prevSDPState = self.__sdpState
                self.__sdpState = SDPState.SDP_RCVD.value
            elif self.__sdpState == SDPState.SDP_SENT.value:
                self.__prevSDPState = self.__sdpState
                self.__sdpState = SDPState.COMPLETE.value

    def getSDPState(self):
        return self.__sdpState


    
        