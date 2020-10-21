import asyncio
from datetime import datetime

async def wash(clothes):
    cloth_type = {'a' : 2, 'b': 3,  'c': 4}
    return_clothes = []
    for cloth in clothes:
        if cloth_type.get(cloth, None) == None:
            wash_time = 5
        else:
            wash_time = cloth_type[cloth]

        execute_time = 0
        while True:
            print(f'Washing cloth {cloth} ... {wash_time - execute_time} time left.')
            await asyncio.sleep(1)
            execute_time += 1
            if execute_time >= wash_time:
                break

        return_clothes.append("wash_" + cloth)
    print('Finish the wash!')
    return return_clothes


async def dry(clothes):
    for cloth in clothes:
        await asyncio.sleep(1)
        print(f'Dry cloth {cloth} ... complete.')
            
async def cleaner(room_nums):
    for room_idx in range(room_nums):
        await asyncio.sleep(1)
        print(f'Clean room idx {room_idx} ... complete.')

async def main():
    clothes = ['a', 'b', 'c', 'd']
    room_nums = 14

    task1 = asyncio.create_task(
        wash(clothes))

    task3 = asyncio.create_task(
        cleaner(room_nums))
    st = datetime.now()
    print(f"started at {st}")

    washed_cloth = await task1
    await dry(washed_cloth)
    await task3
    et = datetime.now()
    print(f"finished at {et}")
    print(f"time for task: {et-st}")

if __name__ == "__main__":
    asyncio.run(main())
