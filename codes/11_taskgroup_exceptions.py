import asyncio
import aiohttp


async def coro_norm():
    return 'Hello world'


async def coro_value_error():
    raise ValueError


async def coro_type_error():
    raise TypeError


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(coro_norm())
            task2 = tg.create_task(coro_value_error())
            task3 = tg.create_task(coro_type_error())

        results = [task1.result(), task2.result(), task3.result()]

    except* ValueError as e:
        print(f'{e=}')

    except* TypeError as e:
        print(f'{e=}')

    else:
        print(f'{results=}')




asyncio.run(main())