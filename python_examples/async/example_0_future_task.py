import asyncio


# async def call():
#     await asyncio.sleep(1)
#     print('Hello')
#
#
# async def caller():
#     await call()  # function caller stop and wait complete function call
#     print('World')


# async def call():
#     await asyncio.sleep(1)
#     print('Hello')
#
#
# async def caller():
#     asyncio.create_task(call())  # create task execute function call, and continue, when task get ready, it execute
#     print('World2')
#     await asyncio.sleep(2)


async def call():
    await asyncio.sleep(1)
    return 'Hello'


async def caller():
    future = asyncio.ensure_future(call())  # or create_task if Python >= 3.7
    while not future.done():
        await asyncio.sleep(0.3)  # or 0 if not need delay
        print(1)
    result = await future
    print(result + ' World')


event_loop = asyncio.get_event_loop()
tasks = asyncio.wait([
    event_loop.create_task(caller()),
])
event_loop.run_until_complete(tasks)
event_loop.close()
