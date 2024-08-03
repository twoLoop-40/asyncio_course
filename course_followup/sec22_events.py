import asyncio


async def worker(event):
    print('Before the wait()')
    await event.wait()
    if event.is_set():
        print('Event is set')


async def coro():
    print('Hello from coro')


async def main():
    event = asyncio.Event()
    tasks = [
        asyncio.create_task(worker(event))
        for _ in range(5)
    ]

    await asyncio.create_task(coro())

    await asyncio.gather(*tasks)


asyncio.run(main())
