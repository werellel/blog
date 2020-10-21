import sys
import time
from datetime import datetime
from datetime import timedelta


def wash(clothes):
    cloth_type = {'a' : 2, 'b': 3,  'c': 4}
    return_clothes = []
    value = None
    check_time = datetime.now()
    for idx, cloth in enumerate(clothes):
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

        if check_time > datetime.now():
            continue
        else:
            recieved = yield None
            if recieved == None:
                recieved = 0
            check_time = datetime.now() + timedelta(seconds=recieved)
    yield return_clothes

def dry(clothes):
    for cloth in clothes:
        time.sleep(1)
        print(f'Dry cloth {cloth} ... complete.')
            
def main() -> None:
    st = datetime.now()
    print(f"started at {st}")

    clothes = ['a', 'b', 'c', 'd']
    gen_wash = wash(clothes)
    while True:
        return_clothes = next(gen_wash)
        if type(return_clothes) == type([]):
            break  
        else:
            print('nothing...')
        gen_wash.send(3)
        
    dry(return_clothes)

    et = datetime.now()
    print(f"finished at {et}")
    print(f"time for task: {et-st}")

if __name__ == "__main__":
    main()