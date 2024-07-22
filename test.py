import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import os



# def func(name):
#     print(f'task {name} is now on!')
#     # Do time intensive stuff...
#     time.sleep(3)
#     return 'Hello, ' + name


# async def main(loop, name):
#     executor = ThreadPoolExecutor()
#     result = await loop.run_in_executor(executor, func, name)
#     print(result)


# if __name__ == "__main__":
#     start = time.time()
#     loop = asyncio.get_event_loop()

#     tasks = [
#         loop.create_task(main(loop, 'jack')),
#         loop.create_task(main(loop, 'rose'))
#     ]


#     loop.run_until_complete(asyncio.gather(*tasks))

#     print("program over!")
#     print(time.time() - start)


####################################################################
# def func(name):
#     print(f'task {name} is now on!')
#     # Do time intensive stuff...
#     time.sleep(3)
#     return 'Hello, ' + name


# async def main(loop, name):
#     result = await loop.run_in_executor(None, func, name)
#     print(result)


# if __name__ == "__main__":
#     start = time.time()
#     loop = asyncio.get_event_loop()
#     loop.set_default_executor(ThreadPoolExecutor())

#     tasks = [
#         loop.create_task(main(loop, 'jack')),
#         loop.create_task(main(loop, 'rose'))
#     ]


#     loop.run_until_complete(asyncio.gather(*tasks))

#     print("program over!")
#     print(time.time() - start)
####################################################################


# def func(a, b):
#     # Do time intensive stuff...
#     return a + b


# async def main(loop):
#     # NOTE: Using `None` as the first parameter designates the `default` Executor.
#     result = await loop.run_in_executor(None, func, "Hello,", " world!")
#     print(result)


# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.set_default_executor(ThreadPoolExecutor())
#     loop.run_until_complete(main(loop))
####################################################################


#max_workers: int | None = None
# 
# executor_1 = ProcessPoolExecutor(max_workers=3)
# executor_2 = ProcessPoolExecutor()

# cpu_count = os.cpu_count()
# print(f"プロセッサ数: {cpu_count}")



