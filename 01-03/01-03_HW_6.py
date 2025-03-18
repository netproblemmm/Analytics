# Задача 6 *. Кинотеатр

# ввод к-ва мальчиков и девочек
boysQty = int(input("Введите к-во мальчиков: "))
girlsQty = int(input("Введите к-во девочек: "))

solution = ''

# проверка возможности решения
if (boysQty > girlsQty * 2) or (girlsQty > boysQty * 2):
    print("Решение невозможно в принципе")

elif boysQty >= girlsQty:
    # Если мальчиков больше или их количество равно количеству девочек
    k = boysQty - girlsQty # Количество лишних мальчиков
    # Вставка лишних мальчиков между девочками
    for bgb in range(k):
        solution += 'BGB'
    # Добавление оставшихся мальчиков и девочек
    for bg in range(girlsQty - k):
        solution += 'BG'
else:
    # Если девочек больше, чем мальчиков
    k = girlsQty - boysQty # Количество лишних девочек
    # Вставка лишних девочек между мальчиками
    for gbg in range(k):
        solution += 'GBG'
    # Добавление оставшихся мальчиков и девочек
    for gb in range(boysQty - k):
        solution += 'GB'

print(solution)