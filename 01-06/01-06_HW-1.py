# Задание 1. Три списка
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

# Задача 1: найти элементы, которые есть в каждом списке
# Решение без использования множеств
new_elems_1_list = []

for i in range(len(array_1)):
    if (array_1[i] in array_2) and (array_1[i] in array_3):
        new_elems_1_list.append(array_1[i])

print('Задача 1. Решение без множеств: ', new_elems_1_list)

# Решение с использованием множеств
new_elems_1_set = set(array_1) & set(array_2) & set(array_3)

print("Задача 1. Решение с множествами:", new_elems_1_set)

# Задача 2: найти элементы из первого списка, которых нет во втором и третьем списках
# Решение без использования множеств
new_elems_2_list = []

for i in range(len(array_1)):
    if (array_1[i] not in array_2) and (array_1[i] not in array_3):
        new_elems_2_list.append(array_1[i])

print('Задача 1. Решение без множеств: ', new_elems_2_list)

# Решение с использованием множеств
new_elems_2_set = set(array_1) - set(array_2) - set(array_3)

print("Задача 1. Решение с множествами:", new_elems_2_set)
