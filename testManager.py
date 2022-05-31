import speedtest
class TestManager:
    def __init__(self, mockData):
        self.promptConfig()
        self.results = []
        self.mockData = mockData
        self.__servers = []
        self.__speedTest = None
        
        
    def speedTest(self):
        
        self.__speedTest = speedtest.Speedtest()
        self.__speedTest.get_servers(self.__servers)
        self.__speedTest.get_best_server()
        
        self.results.append(self.__speedTest.results.download)
        self.results.append(self.__speedTest.results.upload)
        
    def promptConfig(self):
        self.__interval = int(input("Gibe ein interval ein: "))
        self.__execution = int(input("Wie oft würde der Test ausgeführt werden?: "))
        
        
        
    