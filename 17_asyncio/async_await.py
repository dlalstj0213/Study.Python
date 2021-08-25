import asyncio

async def add(x, y):
    print(f"{x} + {y}")
    await asyncio.sleep(1)
    return x + y


async def print_add(x, y):
    ##############################################
    # await으로 네이티브 코루틴 실행 후 반환값 받기
    ##############################################
    result = await add(x, y)
    print(f"print_add: {x} + {y} = {result}")


def main():
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(print_add(2, 3))
    finally:
        loop.close()


if __name__ == "__main__":
    main()
