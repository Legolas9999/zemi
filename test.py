import asyncio
from concurrent.futures import ThreadPoolExecutor  
import time

def func(name):
    print(f'task {name} is now on!')
    # Do time intensive stuff...
    time.sleep(3)
    return 'Hello, ' + name



async def main(loop, name):
    executor = ThreadPoolExecutor()
    result = await loop.run_in_executor(executor, func, name)
    print(result)


if __name__ == "__main__":
    start = time.time()
    loop = asyncio.get_event_loop()

    tasks = [
        loop.create_task(main(loop, 'jack')),
        loop.create_task(main(loop, 'rose'))
    ]

    loop.run_until_complete(asyncio.gather(*tasks))

    print("program over!")
    print(time.time() - start)