import asyncio

from util import async_timed, delay


@async_timed()
async def main():
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))

    await task_one
    await task_two

if __name__ == '__main__':
    asyncio.run(main())
