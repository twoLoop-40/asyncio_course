import asyncio
from aiohttp import ClientSession
from util import async_timed
from util.fetch import fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        url = 'https://www.example.com'
        status = asyncio.create_task(fetch_status(session, url))

        try:
            result_status = await status
            print(f'Status: for {url=} was {result_status=}')

        except Exception as error:
            print(f'{error=}')


if __name__ == '__main__':
    asyncio.run(main())
