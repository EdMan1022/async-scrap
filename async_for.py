import asyncio


async def mygen(u: int = 10):
    """
    Yield powers of 2
    :param u: value to yield up to
    :return: (int) current power of 2
    """

    i = 0
    while i < u:
        yield 2 ** i
        i += 1
        print(f'calculated {i}')
        await asyncio.sleep(1.0)


async def tick(delay, value):
    print(f'Tick #{value}')
    await asyncio.sleep(delay)
    return value


async def ticker(delay, to):
    for i in range(to):
        await asyncio.sleep(delay)
        yield i


async def hello():
    for i in range(20):
        print(f'hello {i}')
        await asyncio.sleep(1)


async def for_loop():
    g = [i async for i in mygen()]
    yield g


async def main():
    res = await asyncio.gather(
        hello(),
        for_loop()
    )
    return res


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
