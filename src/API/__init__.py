import aiohttp
import json

class AsyncRequests:

    def __init__(self) -> None:
        pass

    async def _get(self, url) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                html = await response.json()
                return html
                
    async def _post(self, url, body):
        pass