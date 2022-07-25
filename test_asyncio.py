import time
import asyncio
loop = asyncio.get_event_loop() #建立一個Event Loop

async def example1(): # 定義一個中間會被中斷的協程
    print("Start example1 coroutin.")
    await asyncio.sleep(5) # 中斷協程一秒
    print("Finish example1 coroutin.")

async def example2(): # 定義一個協程
    print("Start example2 coroutin.")
    # do some process...
    print("Finish example2 coroutin.")

tasks = [ # 建立一個任務列表
    asyncio.ensure_future(example1()),
    asyncio.ensure_future(example2()),
]

loop.run_until_complete(asyncio.wait(tasks))
# 把example1, example2這兩個coroutin註冊到事件循環裡
# loop啟動，先執行example1，中途暫停example1之後切換到example2，最後再切回example1
# output:
# Start example1 coroutin.
# Start example2 coroutin.
# Finish example2 coroutin.
# Finish example1 coroutin.