import asyncio
import random

# ANSI colors

COLORS = (
    "\033[0m",
    "\033[36m",
    "\033[91m",
    "\033[35m",
)


async def make_random(idx: int, threshold: int = 6) -> int:

    print(COLORS[idx + 1] + f"Initiated make_random({idx}).")

    i = random.randint(0, 10)
    while i <= threshold:
        print(COLORS[idx + 1] + f"make_random({idx}) == {i} roo low; retrying.")
        await asyncio.sleep(idx + 1)
        i = random.randint(0, 10)
    print(COLORS[idx + 1] + f"---> Finished: make_random({idx}) == {i}" + COLORS[0])
    return i


async def main():
    res = await asyncio.gather(*(make_random(i, 10 - i - 1) for i in range(3)))
    return res

if __name__ == "__main__":
    random.seed(444)
    loop = asyncio.get_event_loop()
    r1, r2, r3 = loop.run_until_complete(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")
