import asyncio
import aiohttp


class WriteToFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file_object = open(self.filename, 'w')
        return self.file_object

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file_object:
            self.file_object.close()



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
        print(f'{url}: {html[:20]}')


async def main():
    await asyncio.create_task(check('https://facebook.com'))
    await asyncio.create_task(check('https://youtube.com'))
    await asyncio.create_task(check('https://google.com'))


asyncio.run(main())