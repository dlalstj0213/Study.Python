import asyncio


async def my_func(val: int):
    for i in range(10):
        await asyncio.sleep(0.5)
        print(i, end=" ")
    return val * val


def main():
    try:
        loop = asyncio.get_event_loop()
        
        ########################
        # 테스크(퓨처) 객체 생성
        ########################
        val = asyncio.ensure_future(my_func(5))
        val2 = asyncio.ensure_future(my_func(6))

        # val.result() 이 위치에서 작성하면 에러 발생함. 왜냐하면 미래의 값을 아직 받지 않았는데 호출하기 때문.
        loop.run_until_complete(asyncio.gather(val, my_func(3), my_func(2), val2))
        print()
        print(val.result())
        print(val2.result())
    finally:
        loop.close()


if __name__ == "__main__":
    main()
