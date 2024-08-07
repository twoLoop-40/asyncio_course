import asyncio
from asyncio_redbook import table
from dotenv import load_dotenv

from util import connection

load_dotenv()


async def main():
    statements = [table.CREATE_BRAND_TABLE,
                  table.CREATE_PRODUCT_TABLE,
                  table.CREATE_PRODUCT_COLOR_TABLE,
                  table.CREATE_PRODUCT_SIZE_TABLE,
                  table.CREATE_SKU_TABLE,
                  table.SIZE_INSERT,
                  table.COLOR_INSERT]

    async with connection.get_connection() as conn:
        print('Creating the product database...')
        for statement in statements:
            status = await conn.execute(statement)
            print(status)


if __name__ == '__main__':
    asyncio.run(main())
