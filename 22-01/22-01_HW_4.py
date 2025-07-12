# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

COUNT_QTY = 10
low_border = 1
high_border = 1000
count = 1

rand_num = randint(low_border, high_border)

while count <= COUNT_QTY + 1:
    a = int(input(f"Введите ваше число от {low_border} до {high_border}: "))
    if a < low_border or a > high_border:
        print(f"Число должно быть в интервале от {low_border} до {high_border} ! Осталось {COUNT_QTY - count} попыток")
        count += 1
        continue
    if a == rand_num:
        print(f"Вы победили с {count} попытки!")
        break
    else:
        if a > rand_num:
            print(f"Искомое число меньше. Осталось {COUNT_QTY - count} попыток")
            count += 1
            high_border = a - 1
        if a < rand_num:
            print(f"Искомое число больше. Осталось {COUNT_QTY - count} попыток")
            count += 1
            low_border = a + 1
        if count == (COUNT_QTY + 1) and a != rand_num:
            print("Вы проиграли!")
            break