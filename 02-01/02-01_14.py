# Имеется список чисел numbers, который содержит значения от 1 до 100.
# Нужно создать новый списко squared_numbers, в который войдут квадраты всех четных чисел из numbers.
# Затем создайте список cubed_numbers, содержащий кубы всех чисел из squared_numbers, которые делятся на 3.
# Вывести сумму всех чисел из cubed_numbers.

numbers = list(range(1, 101))

# Способ 1. Просто циклом
# squared_numbers = []
# for number in numbers:
#     if number % 2 == 0:
#         squared_numbers.append(number ** 2)

# Способ 2. List comprehension
# squared_numbers = [number ** 2 for number in numbers if number % 2 == 0]

# Способ 3. Функции высшего порядка
squared_numbers = list(map(lambda result: result ** 2, filter(lambda number: number % 2 == 0, numbers)))

print(squared_numbers)

cubed_numbers = [number ** 3 for number in squared_numbers if number % 3 == 0]

print(cubed_numbers)

sum_of_cubed_numbers = sum(cubed_numbers)

print(sum_of_cubed_numbers)
