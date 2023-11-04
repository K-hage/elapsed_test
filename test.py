import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


async def fetch_all():
    async with aiohttp.ClientSession() as session:
        resp = await asyncio.gather(*[
            fetch(session, 'http://0.0.0.0:8000/test')
            for i in range(4)
        ])
        return print(resp)


asyncio.run(fetch_all())
