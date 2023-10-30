import aiohttp
from models import Community
from typing import List
from . import AsyncRequests

class RaspisanieAPI(AsyncRequests):

    def __init__(self, communityPrefix:str) -> None:
        self.host = 'http://127.0.0.1:8456'
        self.communityPrefix = communityPrefix

    async def getCommunity(self) -> List[Community]:
        url = self.host + self.communityPrefix
        return (await self._get(url))['data']

    async def getSchedule(self, id):
        url = self.host + '/schedule' + self.communityPrefix + f'/{id}'
        return await self._get(url)

    async def getExam(self, id):
        url = self.host + '/schedule' + self.communityPrefix + f'/{id}'
        return await self._get(url)