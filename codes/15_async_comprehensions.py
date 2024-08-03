import asyncio

from faker import Faker


faker = Faker('en_US')


async def get_user(n=1):
    for i in range(n):
        await asyncio.sleep(0.1)
        name, surname = faker.name_male().split()
        yield name, surname


async def main():
    users_list = [name async for name in get_user(3)]
    # print(users_list)

    users_dict = {name: surname async for name, surname in get_user(3)}
    # print(users_dict)

    users_set = {name async for name in get_user(3)}
    print(users_set)


asyncio.run(main())