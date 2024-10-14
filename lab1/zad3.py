import asyncio

async def foo(time) -> None:
    await asyncio.sleep(time)
    print("foo " + str(time))

async def main() -> None:
    task1 = asyncio.create_task(foo(3))
    task2 = asyncio.create_task(foo(1))
    await task1, task2

if __name__ == "__main__":
    asyncio.run(main())