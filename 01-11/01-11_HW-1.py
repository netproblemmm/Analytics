# Задание 1. Новые списки
from functools import reduce

floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers = [22, 33, 10, 6894, 11, 2, 1]

# floats_new = [round(i ** 3, 3) for i in floats] # простой
floats_new = list(map(lambda x: round(x ** 3, 3), floats)) # сложный

# names_new = [i for i in names if len(i) > 4] # простой
names_new = list(filter(lambda name: len(name) >= 5, names)) # сложный

numbers_new = reduce(lambda num1, num2: num1 * num2, numbers)

print(floats_new)
print(names_new)
print(numbers_new)