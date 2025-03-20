# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
list_1 = [1, 2, 3, 4, 5]
k = int(input())
k = k % len(list_1) # Если k = 6 (больше длины массива), то приводим его к 1 (вычитаем лишние 5 смещений)

list_res = []

for i in reversed(range(k)):
    list_res.append(list_1[len(list_1) - 1 - i])
print(list_res)

for i in range(len(list_1) - k):
    list_res.append(list_1[i])
print(list_res)