import asyncio
from aiohttp import ClientSession
from util import async_timed, fetch_status


@async_timed()
async def main():
    example_url = 'https://example.com'
    async with ClientSession() as session:
        fetchers = [
            asyncio.create_task(fetch_status(session, example_url)) for _ in range(2)
        ]
        done, pending = await asyncio.wait(fetchers)

        print(f'Done task count: {len(done)}')
        print(f'Pending task count: {len(pending)}')

        for done_task in done:
            result = await done_task
            print(result)


if __name__ == '__main__':
    asyncio.run(main())
