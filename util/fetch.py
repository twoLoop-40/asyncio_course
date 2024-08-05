from aiohttp import ClientSession

from util import async_timed

import asyncio


@async_timed()
async def fetch_status(session: ClientSession, url: str, delay: int | None = None) -> int:
    if delay is not None:
        await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status
