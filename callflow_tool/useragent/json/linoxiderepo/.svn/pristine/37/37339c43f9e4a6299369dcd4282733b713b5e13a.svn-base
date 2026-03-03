from sipconstants import TestCaseResult, TestCaseStatus
import json

class TestReport:
    __instance = None
    @staticmethod
    def getInstance():
        return TestReport.__instance if TestReport.__instance else TestReport()
    def __init__(self) -> None:
        self.__status = TestCaseStatus.PENDING.value
        self.__signalingReport:TestCaseResult = TestCaseResult.NONE.value
        self.__reason = ""
        self.__mediaReport:TestCaseResult = TestCaseResult.NONE.value
        self.__result = TestCaseResult.NONE.value
        if TestReport.__instance != None:
            raise Exception("this is a singletonc class")
        else:
            TestReport.__instance = self
            
    def setSignalingReport(self, result:TestCaseResult, reason=""):
        if self.__signalingReport != TestCaseResult.FAIL.value:
            self.__signalingReport = result
            self.__reason = self.__reason + reason if reason else ""
            
    def setMediaReport(self, result:TestCaseResult):
        self.__mediaReport = result
                
    def setResult(self):
        if self.__signalingReport == TestCaseResult.FAIL.value or self.__mediaReport == TestCaseResult.FAIL.value:
            self.__result = TestCaseResult.FAIL.value        
                    
    def setTestCaseStatus(self, status:TestCaseStatus):
        self.__status = status
        
    def getSignalingResult(self):
        return self.__signalingReport, self.__reason
    
    def getMediaResult(self):
        return self.__mediaReport
    
    def getTestReportInJson(self):
        return json.dumps(self.__dict__, indent=4)
        
    
     
    
            