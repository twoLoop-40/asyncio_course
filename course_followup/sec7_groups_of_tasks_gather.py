import asyncio

from utils import ServerError, check


# coros = [
#     check('https://facebook.com'),
#     check('https://google.com'),
#     check('https://twitter.com'),
# ]


async def server_returns_error():
    await asyncio.sleep(2)
    raise ServerError('Failed to get data')


async def main():
    # results = await asyncio.gather(
    #     *coros,
    #     server_returns_error(),
    #     return_exceptions=True
    # )

    # for res in results:
    #     print(res)

    group1 = asyncio.gather(
        check('https://facebook.com'),
        check('https://google.com'),
    )

    group2 = asyncio.gather(
        check('https://google.com'),
        check('https://twitter.com'),
    )
    groups = asyncio.gather(group1, group2)
    results = await groups

    for result in results:
        print(result)


    # for coro in asyncio.as_completed(coros):
    #     result = await coro
    #
    #     print(result)


if __name__ == '__main__':
    asyncio.run(main())
