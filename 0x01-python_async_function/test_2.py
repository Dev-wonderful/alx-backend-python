import asyncio

async def async_function():
    await asyncio.sleep(2)
    return "Async operation completed"

async def main():
    result = await async_function()
    print("2")
    print(result)

asyncio.run(main())
