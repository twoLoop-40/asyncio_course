import asyncio
import aiohttp
from aiohttp import ClientSession


async def fetch_status(session: ClientSession, url: str) -> int:
    ten_mills = aiohttp.ClientTimeout(total=.8)
    async with session.get(url, timeout=ten_mills) as result:
        return result.status


async def main():
    session_timeout = aiohttp.ClientTimeout(total=1, connect=.1)
    async with aiohttp.ClientSession(timeout=session_timeout) as session:
        await fetch_status(session, 'https://example.com')


if __name__ == '__main__':
    asyncio.run(main())