# Producer-Consumer Problem
import asyncio
import random

queue = asyncio.Queue()

async def producer():
    for i in range(1,6):
        await asyncio.sleep(random.uniform(0.5,1.5))
        item = f"Item-{i}"
        await queue.put(item)
        print(f"Produced:{item}")
    await queue.put(None)

async def consumer():
    while True:
        item = await queue.get()
        if item is None:  # Exit signal
            break
        print(f"Consumed: {item}")
        await asyncio.sleep(random.uniform(2, 3))  # Simulate processing

async def main():
    await asyncio.gather(producer(), consumer())

asyncio.run(main())
