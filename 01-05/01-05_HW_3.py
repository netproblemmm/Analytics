# Задача 3. Сортировка
list_1 = [1, 4, -3, 10, 0]
print('Изначальный список: ', list_1)

for i in range(len(list_1) - 1):
    for j in range(len(list_1) - 1 - i):
        if list_1[j] > list_1[j + 1]:
            list_1[j], list_1[j + 1] = list_1[j + 1], list_1[j] 

print('Отсортированный список: ', list_1)
