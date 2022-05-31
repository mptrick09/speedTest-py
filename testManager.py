import speedtest
class TestManager:
    def __init__(self, mockData):
        self.results = []
        self.mockData = mockData
        self.__servers = []
        self.__speedTest = None
        self.__interval = 0
        self.__execution = 0
        
    def speedTest(self):
        
        self.__speedTest = speedtest.Speedtest()
        self.__servers.append(self.__speedTest.get_best_server())
        self.__speedTest.get_best_server()
        threads = None
        self.__speedTest.download(threads=threads)
        self.__speedTest.upload(threads=threads)
        self.__speedTest.results.share()
        
        self.results.append(self.__speedTest.results.dict())
        
    def promptConfig(self):
        self.__interval = int(input("Gibe ein interval ein: "))
        self.__execution = int(input("Wie oft würde der Test ausgeführt werden?: "))
        
        
        
    