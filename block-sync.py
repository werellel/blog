import sys
import time
from datetime import datetime


def wash(clothes):
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
            time.sleep(1)
            execute_time += 1
            if execute_time >= wash_time:
                break
        return_clothes.append("wash_" + cloth)

    print('Finish the wash!')
    return return_clothes

def dry(clothes):
    for cloth in clothes:
        time.sleep(1)
        print(f'Dry cloth {cloth} ... complete.')
            
            
def cleaner(room_nums):
    for room_idx in range(room_nums):
        time.sleep(room_idx)
        print(f'Clean room idx {room_idx} ... complete.')
        
def main() -> None:
    st = datetime.now()
    print(f"started at {st}")

    clothes = ['a', 'b', 'c', 'd']
    clothes = wash(clothes)
    dry(clothes)
    room_nums = 10
    cleaner(room_nums)

    et = datetime.now()
    print(f"finished at {et}")
    print(f"time for task: {et-st}")

if __name__ == "__main__":
    main()