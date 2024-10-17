import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import os
import functools


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


# max_workers: int | None = None
#
# executor_1 = ProcessPoolExecutor(max_workers=3)
# executor_2 = ProcessPoolExecutor()

# cpu_count = os.cpu_count()
# print(f"プロセッサ数: {cpu_count}")

####################################################################


# # event trigger function
# def trigger(event):
#     print('EVENT SET')
#     event.set() # wake up coroutines waiting

# # event consumer_a
# async def consumer_a(event):
#     consumer_name = 'Consumer A'
#     print('{} waiting'.format(consumer_name))
#     await event.wait()
#     print('{} triggered'.format(consumer_name))

# # event consumer_b
# async def consumer_b(event):
#     consumer_name = 'Consumer B'
#     print('{} waiting'.format(consumer_name))
#     await event.wait()
#     print('{} triggered'.format(consumer_name))

# # event
# event = asyncio.Event()

# # wrap coroutines in one future
# main_future = asyncio.wait([consumer_a(event), consumer_b(event)])

# # event loop
# event_loop = asyncio.get_event_loop()
# event_loop.call_later(2, functools.partial(trigger, event)) # trigger event in 0.1 sec

# # complete main_future
# event_loop.run_until_complete(main_future)

####################################################################
# import asyncio
# from aiohttp import ClientSession

# session = ClientSession()  # handles the context manager


# class EchoWebsocket:
#     #
#     async def connect(self):
#         self.websocket = await session.ws_connect("wss://echo.websocket.org")

#     async def send(self, message):
#         self.websocket.send_str(message)

#     async def receive(self):
#         result = await self.websocket.receive()
#         return result.data


# async def main():
#     echo = EchoWebsocket()
#     await echo.connect()
#     await echo.send("Hello World!")
#     print(await echo.receive(), 'hello')  # "Hello World!"


# if __name__ == "__main__":
#     # The main loop
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())

####################################################################
# async def main():

#     async with aiohttp.ClientSession() as session:
#         async with session.get('http://python.org') as response:

#             print("Status:", response.status)
#             print("Content-type:", response.headers['content-type'])

#             html = await response.text()
#             print("Body:", html[:15], "...")

# asyncio.run(main())


####################################################################


# import asyncio
# from aiohttp import ClientSession

# class EchoWebsocket:
#     def __init__(self):
#         self.websocket = None
#         self.session = None

#     async def connect(self):
#         self.session = ClientSession()
#         self.websocket = await self.session.ws_connect("ws://127.0.0.1:8888")

#     async def send(self, message):
#         await self.websocket.send_str(message)  # await the coroutine

#     async def receive(self):
#         result = await self.websocket.receive()
#         return result.data

#     async def close(self):
#         await self.websocket.close()
#         await self.session.close()

# async def main():
#     echo = EchoWebsocket()
#     await echo.connect()
#     await echo.send("Hello World!")
#     result = await echo.receive()
#     print(result) # "Hello World!"
#     await echo.close()

# if __name__ == "__main__":
#     asyncio.run(main())

####################################################################

# from string import punctuation, ascii_letters, digits
# import random

# random.choice()
# random.randint()

# # パスワード生成に用いる文字
# symbols = ascii_letters + digits + punctuation

# # 乱数生成器をインスタンス化
# secure_random = random.SystemRandom()

# # 10文字のパスワードを生成
# password = "".join(secure_random.choice(symbols) for i in range(10))
# print(password)
####################################################################


# import string, secrets

# alphabet = string.ascii_letters + string.digits
# while True:
#     password = "".join(secrets.choice(alphabet) for i in range(10))
#     if (
#         any(c.islower() for c in password)
#         and any(c.isupper() for c in password)
#         and sum(c.isdigit() for c in password) >= 3
#     ):
#         break

# print(password)
# print(sum([True,True,False]))
# print('5'.isdigit())
####################################################################

# from random import SystemRandom

# secure_rand_gen = SystemRandom()

# print([secure_rand_gen.randrange(0, 21) for i in range(10)])

# print(secure_rand_gen.randint(0, 21))

####################################################################

# import os

# # バイトを五つ生成する
# random_bytes = os.urandom(5)
# print(random_bytes)
####################################################################

# import random
# laughs = ["Hi", "Ho", "He"]
# random.shuffle(laughs) 

# print(laughs)
# laughs = random.shuffle(laughs)
# print(laughs)
####################################################################

# import random
# laughs = ["Hi", "Ho", "He"]
# print(random.choice(laughs)) 
####################################################################

# import random
# laughs = ["Hi", "Ho", "He"]
# print(random.sample( laughs , 4 ))  
####################################################################


# import random
# # 1から8まで整数を一つランダムに生成する
# print(random.randint(1, 8))

####################################################################

# import random

# # 0から99の範囲で
# print(random.randrange(100)) 

# # 20から49の範囲で
# print(random.randrange(20, 50)) 

# # 10から19の範囲で、ステップは3
# # 10,13,16,19
# print(random.randrange(10, 20, 3)) 
####################################################################

# import random

# # 0から1の範囲で、一つ浮動小数点数(float)を生成する
# print(random.random())

# # 1から8の範囲で、一つ浮動小数点数(float)を生成する
# print(random.uniform(1, 8))
####################################################################

# import random

# # 整数5で乱数生成器を初期化
# random.seed() 
# # 0から9の範囲で、整数を生成する
# print(random.randrange(0, 10))
# print(random.randrange(0, 10))


# # 整数5で乱数生成器を初期化
# random.seed() 
# # 0から9の範囲で、整数を生成する
# print(random.randrange(0, 10))
# print(random.randrange(0, 10))

####################################################################

# import random

# # 現在の乱数生成器の状態を取得
# save_state = random.getstate() 
# # 0から9の範囲で、整数を生成する
# print(random.randrange(0, 10))
# print(random.randrange(0, 10))

# # 最初の状態にリセットする
# random.setstate(save_state) 
# # 0から9の範囲で、整数を生成する
# print(random.randrange(0, 10))
# print(random.randrange(0, 10))
####################################################################
# import random

# # リセット
# random.seed(None)
# print(random.randint(0, 10))
# print(random.randint(0, 10))

# # リセット
# random.seed()
# print(random.randint(0, 10))
# print(random.randint(0, 10))

# # リセット
# random.seed(None)
# print(random.randint(0, 10))
# print(random.randint(0, 10))
####################################################################


# import random

# # 確率を指定
# probability = 0.3
# decision_1 = 0
# decision_2 = 0
# for i in range(10000):
#     # ランダムに0から1まで小数を生成する
#     if random.random() < probability:
#         #print("Decision_1 with probability 0.3")
#         decision_1 += 1
#     else:
#         #print("Decision_2 with probability 0.7")
#         decision_2 += 1

# print(decision_1, decision_2)

####################################################################


from string import punctuation, ascii_letters, digits
import random
# 句読点　print(punctuation)

# アルファベット　print(ascii_letters)

# 数字　print(digits)

# パスワード生成に用いる文字
symbols = ascii_letters + digits + punctuation
# 乱数生成器をインスタンス化
secure_random = random.SystemRandom()
# 10文字のパスワードを生成
password = "".join(secure_random.choice(symbols) for i in range(10))

print(password)


#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
symbol = "-"
seq = ("a", "b", "c") # 字符串序列
print ("".join( seq ))

print(secure_random.choice(symbols) for i in range(10))

gen = (secure_random.choice(symbols) for i in range(10))

for i in gen:
    print(i)