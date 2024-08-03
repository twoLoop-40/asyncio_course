from typing import TextIO
import asyncio

from utils import check


class WriteToFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> TextIO:
        self.file_object = open(self.filename, 'w')
        return self.file_object

    def __exit__(self, exc_type, exc_val, traceback):
        if self.file_object:
            self.file_object.close()


# def main():
#     with WriteToFile('text.txt') as f:
#         f.write('Hello World!')


async def main():
    await asyncio.create_task(check('https://facebook.com'))
    await asyncio.create_task(check('https://youtube.com'))
    await asyncio.create_task(check('https://www.google.com'))


if __name__ == '__main__':
    asyncio.run(main())
