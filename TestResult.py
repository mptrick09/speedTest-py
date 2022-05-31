import speedtest
class TestResult:
    def __init__(self, timestamp):
        self.download = 0
        self.upload = 0
        self.timestand = timestamp
        
    def __str__(self):
        return " Timestamp ".format(self.timestand)
            
    def convertToMBits(self, bits):
        Megabits = bits / 1048576  
        return round(Megabits, 4)
    def setDownload(self):
        s = speedtest.Speedtest()
        self.download = s.download()
        
    def getDownloadinMbits(self):
        return self.download
    
    def setUpload(self):
        s = speedtest.Speedtest()
        self.upload = s.upload()
        
    def getUploadinMbits(self):
        return self.updoad