import asyncio
from random import randint


async def waiter(condition, id):
    async with condition:
        print(f'Waiter {id} is awaiting')
        await condition.wait()

        num = randint(1, 5)
        print(f'Waiter {id} generated {num}')


async def starter(condition):
    print('Waiting for 5 seconds')
    await asyncio.sleep(5)

    async with condition:
        condition.notify(2)


async def main():
    condition = asyncio.Condition()

    waiters = [
        asyncio.create_task(waiter(condition, id=i))
        for i in range(5)
    ]

    asyncio.create_task(starter(condition))

    await asyncio.gather(*waiters)






asyncio.run(main())
