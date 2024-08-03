import asyncio


async def coro(message):
    print(message)
    await asyncio.sleep(1)
    print(message)


async def main():
    # print(asyncio.all_tasks())

    print('-- main beginning')
    asyncio.create_task(coro('text'))
    # print(asyncio.all_tasks())

    await asyncio.sleep(0.5)
    print('-- main done')


asyncio.run(main())