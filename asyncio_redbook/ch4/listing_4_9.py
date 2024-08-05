import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed, fetch_status


@async_timed()
async def main():
    example_url = 'https://example.com'
    async with ClientSession() as session:
        fetchers = [fetch_status(session, example_url, 1),
                    fetch_status(session, example_url, 10),
                    fetch_status(session, example_url, 10)]

        for done_task in asyncio.as_completed(fetchers, timeout=2):
            try:
                result = await done_task
                print(result)
            except asyncio.TimeoutError:
                print('We got a timeout error!')

        for task in asyncio.all_tasks():
            print(task)

if __name__ == '__main__':
    asyncio.run(main())
    