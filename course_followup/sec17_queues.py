import asyncio
from random import randint


class Color:
    norm = '\033[0m'
    blue = '\033[94m'
    green = '\033[92m'


color = Color()


async def producer(queue, name):
    timeout = randint(1, 5)
    await queue.put(timeout)
    # await asyncio.sleep(timeout)
    print(f'{color.blue}Producer {name} put {timeout} to the queue: {queue}{color.norm}')


async def consumer(queue, name):
    while True:
        timeout = await queue.get()
        await asyncio.sleep(timeout)
        print(f'{color.green}Consumer {name} ate {timeout}, queue:{queue}{color.norm}')
        queue.task_done()


async def main():
    queue = asyncio.Queue(maxsize=4)

    producers = []
    for i in range(12):
        task = asyncio.create_task(producer(queue, name=i))
        producers.append(task)

    consumers = []
    for i in range(4):
        task = asyncio.create_task(consumer(queue, name=i))
        consumers.append(task)

    await asyncio.gather(*producers)
    await queue.join()

    for c in consumers:
        c.cancel()


if __name__ == '__main__':
    asyncio.run(main())
