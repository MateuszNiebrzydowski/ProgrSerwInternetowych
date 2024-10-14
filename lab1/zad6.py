import asyncio


async def fetch(delay: int):
    await asyncio.sleep(delay)
    return "Dowolna wartość"

async def main():
    task1 = asyncio.create_task(fetch(2))
    task2 = asyncio.create_task(fetch(1))
    task3 = asyncio.create_task(fetch(3))
    task4 = asyncio.create_task(fetch(7))
    results = await asyncio.gather(task1, task2, task3, task4)
    print(results)

if __name__ == "__main__":
    asyncio.run(main())