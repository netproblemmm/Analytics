# К-во пар элементов, равных друг другу
list_1 = [1, 2, 3, 2, 3]
count = 0

for i in range(len(list_1)):
    for j in range(i + 1, len(list_1)):
        if i != j and list_1[i] == list_1[j]:
            count += 1
print(count)