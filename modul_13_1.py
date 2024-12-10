import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 5):
         await asyncio.sleep(6 - power)
         print(f'Силач {name} поднял шар номер {i}.')
    print(f'Силач {name} закончил соревнования.')

async  def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Pasha', 3))
    task_2 = asyncio.create_task(start_strongman('Denis', 4))
    task_3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task_1
    await task_2
    await task_3

asyncio.run(start_tournament())
