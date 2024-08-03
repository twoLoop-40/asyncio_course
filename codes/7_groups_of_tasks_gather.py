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


class ServerError(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message


async def server_returns_error():
    await asyncio.sleep(3)
    raise ServerError('Failed to get data')


async def check(url):
    async with AsyncSession(url) as response:
        html = await response.text()
        return f'{url}: {html[:20]}'


async def main():
    # facebook_res = await asyncio.create_task(check('https://facebook.com'))
    # youtube_res = await asyncio.create_task(check('https://facebook.com'))
    # google_res = await asyncio.create_task(check('https://google.com'))
    # res0 = await asyncio.create_task(check('https://lkjlkj.com'))

    # print(facebook_res)
    # print(youtube_res)
    # print(google_res)

    coros = [
        check('https://facebook.com'),
        check('https://youtube.com'),
        check('https://google.com')
    ]

    group1 = asyncio.gather(
        check('https://facebook.com'),
        check('https://youtube.com'),
    )

    group2 = asyncio.gather(
        check('https://youtube.com'),
        check('https://google.com')
    )
    print(type(group2))

    groups = asyncio.gather(group1, group2)

    results = await groups

    for res in results:
        print(res)





    # for coro in asyncio.as_completed(coros):
    #     result = await coro

    #     print(result)

    # results = await asyncio.gather(
    #     *coros,
    #     server_returns_error(),
    #     return_exceptions=True
    # )

    # for res in results:
    #     print(res)


asyncio.run(main())