from asyncio.tasks import wait, wait_for
import time
import asyncio


def sync_func():
    """
    동기적 함수, 0.5초마다 10번 카운트한다.
    """
    for i in range(10):
        time.sleep(0.5)
        print(i, end=" ")


async def my_async_func():
    """
    Native 코루틴, 0.5초마다 10번 카운트한다.
    """
    for i in range(10):
        ################################################################
        # 이벤트 루프를 블락하지 않는 비동기 함수. 그래서 await 붙여줘야 함
        ################################################################
        await asyncio.sleep(0.5)
        print(i, end=" ")


def main():
    try:
        #########################
        # 이벤트 루프 객체를 얻음
        #########################
        loop = asyncio.get_event_loop()

        ###########################
        # TEST 1 : 한 번 실행시
        ###########################
        #
        #
        print("### TEST 1 : 한 번 실행시")
        start = time.time()

        sync_func()

        end = time.time()
        print(f"\nrun def time: {end - start}")

        start = time.time()

        ########################################
        # Native 코루틴 실행이 끝날 때까지 기다림
        ########################################
        loop.run_until_complete(my_async_func())

        end = time.time()
        print(f"\nrun async def time: {end - start}")
        #
        #
        ###########################################
        # TEST 1 결과:
        # run def time: 5.094561576843262
        # run async def time: 5.07861590385437
        # 한 번 실행 결과로는 별차이 없음
        ###########################################

        print()

        ########################################
        # TEST 2 : 여러번 실행시 (예제 3번 실행)
        ########################################
        #
        #
        print("### TEST 2 : 여러번 실행시 (예제 3번 실행)")
        start = time.time()

        sync_func()
        sync_func()
        sync_func()

        end = time.time()
        print(f"\nrun def time: {end - start}")

        start = time.time()

        ################################################################
        # Native 코루틴을 여러번 동시 실행하고 모두 다 끝날 때까지 기다림
        ################################################################
        loop.run_until_complete(
            asyncio.gather(my_async_func(), my_async_func(), my_async_func())
        )

        end = time.time()
        print(f"\nrun async def time: {end - start}")
        #
        #
        ###########################################
        # TEST 2 결과:
        # run def time: 15.311195373535156
        # run async def time: 5.113542079925537
        # 실행 결과가 3배 차이남
        ###########################################

    finally:
        #########################
        # 이벤트 루프 닫아줌
        ##########################
        loop.close()


if __name__ == "__main__":
    main()
