from contextlib import contextmanager, asynccontextmanager
import asyncio

from redis import asyncio as aioredis


@contextmanager
def custom_open(filename, mode: str | None = None):
    if mode is None:
        mode = 'w'
    file_obj = open(filename, mode)
    yield file_obj
    file_obj.close()


@asynccontextmanager
async def redis_connection():
    redis = None
    try:
        redis = await aioredis.from_url('redis://localhost')
        yield redis

    finally:
        if redis:
            await redis.aclose()


async def main():
    async with redis_connection() as redis:
        await redis.set('my_key', 'asyncio course')


if __name__ == '__main__':
    asyncio.run(main())
