class TestResult:
    def __init__(self, download, upload, timestamp):
        self.download = download
        self.upload = upload
        self.timestand = timestamp
        
    def __str__(self):
        return " Timestamp ".format(self.timestand)
            
    def convertToMBits(self, bits):
        Megabits = bits / 1048576  
        return round(Megabits, 4)
    
    def getDownloadinMbits(self, download):
        return self.download
        
    def getUploadinMbits(self, upload):
        return self.updoad 