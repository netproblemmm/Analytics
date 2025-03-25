# Два массива
n = int(input())
list_1 = list()

for i in range(n):
    x = int(input())
    list_1.append(x)

m = int(input())
list_2 = list()

for i in range(m):
    x = int(input())
    list_2.append(x)

count = 0
for i in range(n):
    for j in range(m):
        if list_1[i] == list_2[j]:
            count += 1
    if count == 0:
        print(list_1[i])
    count = 0