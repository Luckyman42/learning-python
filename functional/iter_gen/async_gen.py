import asyncio
from typing import AsyncGenerator, Any
import time

async def agen(begin : int, end : int, sep: int):
    for i in range(begin, end, sep):
        await asyncio.sleep(1)
        yield i

async def worker(ag : AsyncGenerator[int, Any]):
    async for i in ag:
        print(i)

async def main():
    even = agen(0,10,2)
    odd = agen(1,10,2)

    start = time.perf_counter()
    async with asyncio.TaskGroup() as tg:
        tg.create_task(worker(even))
        tg.create_task(worker(odd))
    end = time.perf_counter()
    diff = end-start
    print(f"END in {diff:.6f}")
        

asyncio.run(main())

