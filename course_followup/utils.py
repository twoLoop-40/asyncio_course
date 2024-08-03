import aiohttp


class ServerError(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message


class AsyncSession:
    def __init__(self, url: str) -> None:
        self.url = url
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        response = await self.session.get(self.url)
        return response

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()


async def check(url: str) -> None:
    async with AsyncSession(url) as response:
        html = await response.text()
        return f'{url}: {html[:25]}'


async def coro_norm():
    return 'Hello World!'


async def coro_value_error():
    raise ValueError


async def coro_type_error():
    raise TypeError
