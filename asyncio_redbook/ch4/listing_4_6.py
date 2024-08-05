import asyncio
import aiohttp
from aiohttp import ClientSession
from util import fetch_status, async_timed


# @async_timed()
# async def main():
#     async with ClientSession() as session:
#         urls = ['https://www.example.com' for _ in range(1000)]
#         requests = [fetch_status(session, url) for url in urls]
#         status_codes = await asyncio.gather(*requests)
#         print(status_codes)


@async_timed()
async def main():
    async with ClientSession() as session:
        urls = ['https://www.example.com', 'python://example.com']
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)


if __name__ == '__main__':
    asyncio.run(main())
