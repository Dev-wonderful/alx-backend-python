import asyncio

async def async_function():
    await asyncio.sleep(2)
    print("hello")
    return "Async operation completed"

async def create_and_run_task():
    task = asyncio.create_task(async_function())
    return task

async def main():
    task = await create_and_run_task()
    print("2")
    # Continue with other work concurrently
    await asyncio.sleep(1)
    result = await task
    print(result)

asyncio.run(main())
