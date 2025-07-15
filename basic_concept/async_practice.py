import asyncio

async def print_no():
    for num in range(1,6):
        await asyncio.sleep(1)
        print(f"Number:{num}")

async def print_letter():
    for letter in range(ord("A"), ord("F")):
        await asyncio.sleep(1)
        print(f"Letter:{chr(letter)}")

async def main():
    await asyncio.gather(
        print_no(),
        print_letter()
    )

asyncio.run(main())