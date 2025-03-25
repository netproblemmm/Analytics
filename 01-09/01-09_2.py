# К-во элементов, у которых соседние меньше
n = int(input())
list_1 = list()

for i in range(n):
    x = int(input())
    list_1.append(x)

count = 0

for i in range(1, n - 1):
    if list_1[i - 1] < list_1[i] > list_1[i + 1]:
            count += 1
print(count)