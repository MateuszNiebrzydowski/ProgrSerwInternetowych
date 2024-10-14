import asyncio

async def process(file):
    await asyncio.sleep(2)
    print(f"Odczytano plik {file}")
    await asyncio.sleep(4)
    print(f"Przeanalizowano plik {file}")
    await asyncio.sleep(1)
    print(f"Zapisano plik {file}")

async def main():
    task1 = asyncio.create_task(process(1))
    task2 = asyncio.create_task(process(2))
    task3 = asyncio.create_task(process(3))
    task4 = asyncio.create_task(process(4))
    task5 = asyncio.create_task(process(5))

    await asyncio.gather(task1, task2, task3, task4, task5)

if __name__ == '__main__':
    asyncio.run(main())