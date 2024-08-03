import asyncio

from fastapi import FastAPI

app = FastAPI()

lock = asyncio.Lock()

count = 0

@app.get("/")
async def main():
    global count

    async with lock:
        count += 1

    return dict(count=count)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("server:app", reload=True)
