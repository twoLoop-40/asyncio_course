import asyncio

from faker import Faker

faker = Faker('en_US')


async def get_user(n=1):
    for i in range(n):
        name, surname = faker.name_male().split()
        yield name, surname


async def main():
    users_list = [name async for name in get_user(n=3)]
    print(users_list)

    users_dict = {name: surname async for name, surname in get_user(n=3)}
    print(users_dict)


if __name__ == '__main__':
    asyncio.run(main())



