import asyncio

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


async def main() -> None:
    n = int(input("Podaj N: "))
    counter = 0
    while counter <= n:
        await asyncio.sleep(1)
        print(fibonacci(counter))
        counter += 1

if __name__ == "__main__":
    asyncio.run(main())
