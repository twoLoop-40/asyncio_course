import asyncio
import aiohttp



class AsyncSession:
    def __init__(self, url):
        self.url = url

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        response = await self.session.get(self.url)
        return response

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.session.close()


async def check(url):
    async with AsyncSession(url) as response:
        html = await response.text()
        return f'{url}: {html[:20]}'


async def main():
    # await asyncio.create_task(check('https://facebook.com'))
    # await asyncio.create_task(check('https://youtube.com'))
    # await asyncio.create_task(check('https://google.com'))

    async with asyncio.TaskGroup() as tg:
        print(type(tg))
        print(dir(tg))
        print()

        task1 = tg.create_task(check('https://facebook.com'))
        task2 = tg.create_task(check('https://youtube.com'))
        task3 = tg.create_task(check('https://google.com'))

    print(task1.result())
    print(task2.result())
    print(task3.result())


asyncio.run(main())