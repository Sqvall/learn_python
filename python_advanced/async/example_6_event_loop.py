import asyncio


async def async_worker(seconds):
    print(f'Sleep using {seconds}')
    await asyncio.sleep(seconds)
    print(f'Done sleep: {seconds}')


async def stop_event_loop(loop, seconds):
    print(f'Stop in {seconds}s')
    await asyncio.sleep(seconds)
    loop.stop()
    print(f'Stopped')


async def resolve_future(future):
    await asyncio.sleep(5)
    print('Future set_result')
    future.set_result(10)


async def wait_for_future(future):
    result = await future
    print(f'Future result: {result}')


event_loop = asyncio.get_event_loop()

# fut = event_loop.create_future()
fut = asyncio.Future()

event_loop.create_task(async_worker(3))
event_loop.create_task(async_worker(4))
# event_loop.create_task(stop_event_loop(event_loop, 10))
event_loop.create_task(stop_event_loop(event_loop, 3))
event_loop.create_task(resolve_future(fut))
event_loop.create_task(wait_for_future(fut))
event_loop.run_forever()
event_loop.close()
