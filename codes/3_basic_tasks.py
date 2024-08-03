import asyncio


async def one():
    return 1


async def greet(timeout):
    await asyncio.sleep(timeout)
    return 'Hello world'


async def main():
    res1 =  asyncio.create_task(one())
    res2 =  asyncio.create_task(greet(2))
    res3 =  asyncio.create_task(greet(3))
    res4 =  asyncio.create_task(greet(4))
    res5 =  asyncio.create_task(greet(2))
    res6 =  asyncio.create_task(greet(3))

    print(await res1)
    print(await res2)
    print(await res3)
    print(await res4)
    print(await res5)
    print(await res6)

asyncio.run(main())
