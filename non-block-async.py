import asyncio
from datetime import datetime

async def wash(cloth):
    cloth_type = {'a' : 2, 'b': 3,  'c': 4}
    return_clothes = []
    execute_time = 0

    if cloth_type.get(cloth, None) == None:
        wash_time = 5
    else:
        wash_time = cloth_type[cloth]

    while True:
        print(f'Washing cloth {cloth} ... {wash_time - execute_time} time left.')
        await asyncio.sleep(1)
        execute_time += 1
        if execute_time >= wash_time:
            break
    await dry("wash_" + cloth)


async def dry(cloth):
    await asyncio.sleep(2)
    print(f'Dry cloth {cloth} ... complete.')
            
async def cleaner(room_nums):
    for room_idx in range(room_nums):
        await asyncio.sleep(1)
        print(f'Clean room idx {room_idx} ... complete.')

async def main():
    clothes = ['a', 'b', 'c', 'd']
    room_nums = 10

    st = datetime.now()
    print(f"started at {st}")
    tasks = []
    
    for cloth in clothes:
        tasks.append(asyncio.create_task(
            wash(cloth)))

    tasks.append(asyncio.create_task(
        cleaner(room_nums)))

    for tmp_task in tasks:
        await tmp_task

    et = datetime.now()
    print(f"finished at {et}")
    print(f"time for task: {et-st}")

if __name__ == "__main__":
    asyncio.run(main())
