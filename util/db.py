import os
from contextlib import asynccontextmanager

import asyncpg
from pydantic import BaseModel, Field

from dotenv import load_dotenv

load_dotenv()


class ConnectDB(BaseModel):
    host: str = '127.0.0.1'
    port: int = 5432
    user: str = Field(default=os.getenv('POSTGRES_USERNAME'))
    database: str = Field(default=os.getenv('POSTGRES_DATABASE'))
    password: str = Field(default=os.getenv('POSTGRES_PASSWORD'))

    @asynccontextmanager
    async def get_connection(self):
        conn = None
        try:
            # 환경 변수
            print(
                f'Trying to connect with: host={self.host}, port={self.port}, user={self.user}, '
                f'database={self.database}, password={self.password}')

            # 연결
            conn = await asyncpg.connect(
                host=self.host, port=self.port,
                user=self.user, database=self.database,
                password=self.password
            )

            # 성공
            print('Successfully connected to the database')
            yield conn
        except Exception as error:
            print(f'Could not connect to database: {error=}')

        finally:
            if conn:
                # 닫음
                print('Finished creating the product database!')
                await conn.close()


# 싱글톤
connection = ConnectDB()
