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
        results = await asyncio.gather(
            coro_norm(),
            coro_value_error(),
            coro_type_error(),
            return_exceptions=True
        )

    except ValueError as e:
        print(f'{e=}')

    except TypeError as e:
        print(f'{e=}')

    else:
        print(f'{results=}')




asyncio.run(main())