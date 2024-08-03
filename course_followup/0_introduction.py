import asyncio


async def one():
    return 1


async def greet(timeout):
    await asyncio.sleep(timeout)
    return 'Hello World!'


async def main():
    results = await asyncio.gather(one(), greet(1), greet(2))
    print(results)

asyncio.run(main())
