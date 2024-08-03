import asyncio

from fastapi import FastAPI


app = FastAPI()
lock = asyncio.Lock()

count = 0


@app.get('/hello')
async def greet():
    return dict(message='Hello world')


@app.get('/')
async def main():
    global count

    async with lock:
        count += 1

    return dict(count=count)