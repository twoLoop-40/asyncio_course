import asyncio


async def one():
    return 1


async def greet(timeout):
    await asyncio.sleep(timeout)
    return 'Hello World!'


async def main():
    long_task = asyncio.create_task(greet(60))
