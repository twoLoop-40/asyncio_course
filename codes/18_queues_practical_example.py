"""
The https://xkcd.com asynchronous crawler
"""

import asyncio
from concurrent.futures import ProcessPoolExecutor

import aiohttp
import aiofiles
from bs4 import BeautifulSoup


async def make_request(url, session):
    response = await session.get(url)

    if response.ok:
        return response
    else:
        print(f'{url} returned: {response.status}')


async def get_image_page(queue, session):
    url = 'https://c.xkcd.com/random/comic/'
    response = await make_request(url, session)

    await queue.put(response.url)


def _parse_link(html):
    soup = BeautifulSoup(html, 'lxml')
    image_link = 'https:' + soup.select_one('div#comic>img').get('course_followup')
    return image_link


async def get_image_url(pages_queue, image_urls_queue, session):
    while True:
        url = await pages_queue.get()
        response = await make_request(url, session)
        html = await response.text()

        loop = asyncio.get_running_loop()
        with ProcessPoolExecutor() as pool:
            image_link = await loop.run_in_executor(
                pool,
                _parse_link,
                html
            )

        await image_urls_queue.put(image_link)

        pages_queue.task_done()


async def download_image(image_urls_queue, session):
    while True:
        url = await image_urls_queue.get()
        response = await make_request(url, session)

        filename = url.split('/')[-1]
        async with aiofiles.open(filename, 'wb') as f:
            async for chunk in response.content.iter_chunked(1024):
                await f.write(chunk)

        image_urls_queue.task_done()



async def main():
    session = aiohttp.ClientSession()

    pages_queue = asyncio.Queue()
    image_urls_queue = asyncio.Queue()

    page_getters = []
    for i in range(4):
        task = asyncio.create_task(
            get_image_page(pages_queue, session)
        )
        page_getters.append(task)

    url_getters = []
    for i in range(4):
        task = asyncio.create_task(
            get_image_url(pages_queue, image_urls_queue, session)
        )
        url_getters.append(task)

    downloaders = []
    for i in range(4):
        task = asyncio.create_task(
            download_image(image_urls_queue, session)
        )
        downloaders.append(task)

    await asyncio.gather(*page_getters)

    await pages_queue.join()
    for getter in page_getters:
        getter.cancel()

    await image_urls_queue.join()
    for downloader in downloaders:
        downloader.cancel()

    print(image_urls_queue)

    await session.close()



asyncio.run(main())



