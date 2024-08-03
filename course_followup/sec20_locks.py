import asyncio
import time

import aiohttp

lock = asyncio.Lock()


async def make_request(url):
    async with aiohttp.ClientSession() as session:
        async with lock:
            async with session.get(url) as response:
                data = await response.json()
                print(data)


async def get_data(url):
    await make_request(url)


async def main():
    start = time.perf_counter()

    tasks = [
        asyncio.create_task(get_data('http://localhost:8000'))
        for _ in range(20)
    ]

    await asyncio.gather(*tasks)

    print(time.perf_counter() - start)


asyncio.run(main())
