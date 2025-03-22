# Задача 2. Замена оценок
n = int(input())

list_1 = list()
for i in range(n):
    x = int(input())
    list_1.append(x)

max_n = max(list_1)
min_n = min(list_1)

for i in range(len(list_1)):
    if list_1[i] == max_n:
       list_1[i] = min_n

print(list_1)