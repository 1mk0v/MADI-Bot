import aiohttp

class RaspisanieAPI:
    
    def __init__(self, communityPrefix) -> None:
        self.host = '127.0.0.1:8000'
        self.communityPrefix = communityPrefix

    async def getCommunity(self):
        url = self.host + self.communityPrefix
        print(url)
        pass

    async def getSchedule(self, id):
        url = self.host + '/schedule' + self.communityPrefix + f'/{id}'
        print(url)
        pass

    async def getExam(self, id):
        url = self.host + '/schedule' + self.communityPrefix + f'/{id}'
        print(url)
        pass