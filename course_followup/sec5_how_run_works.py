import asyncio


async def coro(message):
    print(message)
    await asyncio.sleep(1)
    print(message)


async def main():
    print('-- main beginning')
    asyncio.create_task(coro('text'))

    await asyncio.sleep(0.5)
    print('-- main end')

if __name__ == '__main__':
    asyncio.run(main())
