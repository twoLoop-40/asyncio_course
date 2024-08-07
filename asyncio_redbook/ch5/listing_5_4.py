import asyncpg
import asyncio
from asyncpg import Record


async def main():
    levis = "INSERT INTO brand VALUES (DEFAULT, 'Levis')"
    seven = "INSERT INTO brand VALUES (DEFAULT, 'Seven')"

    brand_query = 'SELECT brand_id, brand_name FROM brand'
