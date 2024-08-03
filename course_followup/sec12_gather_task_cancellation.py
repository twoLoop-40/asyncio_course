import asyncio

from utils import coro_norm, coro_value_error


async def coro_long():
    try:
        print('Long task is running...')
        await asyncio.sleep(2)
        return 'Long task result'
    except asyncio.CancelledError:
        print('All needed actions are done')
        raise asyncio.CancelledError


async def main():
    task1 = asyncio.create_task(coro_norm())
    task2 = asyncio.create_task(coro_value_error())
    task3 = asyncio.create_task(coro_long())
    task3.set_name('coro_long')
    tasks = [task1, task2, task3]
    try:
        results = await asyncio.gather(*tasks)

    except ValueError as e:
        print(f'{e=}')

    except TypeError as e:
        print(f'{e=}')

    else:
        print(f'{results=}')

    for task in tasks:
        if task.done() is False:
            task.cancel()
            print(f'Pending: {task.get_name()}')

    await asyncio.sleep(2)


if __name__ == '__main__':
    asyncio.run(main())