import asyncio
import time

async def work(machine, cycle_time):
    start_time = time.time()
    cycle_count = 0
    while True:
        cycle_start = time.time()
        print(f"Maszyna {machine} rozpoczyna cykl {cycle_count + 1}")
        await asyncio.sleep(cycle_time)
        cycle_end = time.time()
        print(f"Maszyna {machine} kończy cykl {cycle_count + 1}")

        cycle_count += 1

        if cycle_end - start_time >= 15:
            break

    print(f"Maszyna {machine} zakończyła pracę po {cycle_count} cyklach")

async def main():
    task1 = asyncio.create_task(work("A", 2))
    task2 = asyncio.create_task(work("B", 3))
    task3 = asyncio.create_task(work("C", 5))

    await asyncio.sleep(15)
    await asyncio.gather(task1, task2, task3)

if __name__ == "__main__":
    asyncio.run(main())