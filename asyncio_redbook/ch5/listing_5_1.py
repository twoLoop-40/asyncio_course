import os

import asyncpg
import asyncio
from dotenv import load_dotenv

load_dotenv()


async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user=os.getenv('POSTGRES_USERNAME'),
                                       database=os.getenv('POSTGRES_DATABASE'),
                                       password=os.getenv('POSTGRES_PASSWORD'))

    version = connection.get_server_version()
    print(f'Connected to Postgres {version=}')
    await connection.close()

if __name__ == '__main__':
    asyncio.run(main())
