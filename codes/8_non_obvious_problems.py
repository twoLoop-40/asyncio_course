import asyncio


async def nothing():
    await asyncio.sleep(0)
    print('Busy')


async def busy_loop():
    for i in range(10):
        await nothing()


async def normal():
    for i in range(10):
        await asyncio.sleep(0)
        print('Normal coroutine')


async def main():
    await asyncio.create_task(busy_loop())
    await asyncio.create_task(normal())

    # await asyncio.gather(
    #     busy_loop(),
    #     normal()
    # )


asyncio.run(main())