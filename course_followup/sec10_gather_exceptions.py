import asyncio

from sec12_gather_task_cancellation import coro_long
from utils import coro_norm, coro_value_error, coro_type_error


async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            coros = [coro_norm(), coro_value_error(), coro_type_error(), coro_long()]
            tasks = [tg.create_task(coro) for coro in coros]

        results = [task.result() for task in tasks]

    except* ValueError as e:
        print(f'{e=}')

    except* TypeError as e:
        print(f'{e=}')

    else:
        print(f'{results=}')

if __name__ == '__main__':
    asyncio.run(main())
