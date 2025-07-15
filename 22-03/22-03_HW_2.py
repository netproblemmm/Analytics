'''
2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
'''

list_1 = [1, 3, 2, 5, 2, 4, 6, 3, 2, 7, 4]

set_unique = set(list_1)
list_duble = []

[list_duble.append(i) for i in set_unique if list_1.count(i) > 1]

print(f'Список дубликатов: {list_duble}')
