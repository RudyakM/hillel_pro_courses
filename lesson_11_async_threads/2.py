import asyncio


async def get_primes_amount(num: int) -> int:
    result = 1
    for i in range(2, num + 1):
        if i % 2 == 0:
            pass
        else:
            result += 1
            for j in range(2, i):
                if i % j == 0:
                    result -= 1
                    break
        await asyncio.sleep(0)

    return result


numbers = [40000, 400, 10000, 700, 50]
tasks = [get_primes_amount(i) for i in numbers]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()
