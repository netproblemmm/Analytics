# Lesson_01: Task_05 (4.2*)
import random
import time

random.seed(5)
list1 = [random.randint(0, 100) for i in range(5)]
print(list1)

def gener(data: list) -> list:
    last_time = time.time()
    list_res = []

    for i in data:
        list_res.append((i, int(time.time() - last_time)))
        last_time = time.time()
        time.sleep(2)

    return list_res

print(*gener(list1))

