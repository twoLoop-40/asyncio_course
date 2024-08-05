import asyncio
from aiohttp import ClientSession
from util import async_timed, fetch_status


@async_timed()
async def main():
    example = 'https://www.example.com'
    async with ClientSession() as session:
        fetchers = [
            fetch_status(session, example, 10),
            fetch_status(session, example, 1),
            fetch_status(session, example, 1)
        ]

        for finished_task in asyncio.as_completed(fetchers):
            print(await finished_task)


if __name__ == '__main__':
    asyncio.run(main())
