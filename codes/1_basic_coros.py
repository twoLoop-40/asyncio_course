import asyncio


async def one():
    return 1


async def greet():
    await asyncio.sleep(2)
    return 'Hello world'


async def main():
    res1 = await one()
    res2 = await greet()

    print(res1)
    print(res2)

asyncio.run(main())
