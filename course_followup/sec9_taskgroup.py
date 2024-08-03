import asyncio

from utils import check

urls = [
    'https://facebook.com',
    'https://google.com',
    'https://twitter.com',
]


async def main():
    async with asyncio.TaskGroup() as tg:
        checks = [check(url) for url in urls]
        tasks = [tg.create_task(check_url) for check_url in checks]
    for task in tasks:
        print(task.result())


if __name__ == '__main__':
    asyncio.run(main())
