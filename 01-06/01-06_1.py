stroka = input().split()
res = {}

for i in stroka:
    if i in res:
        print(f'{i}_{res[i]}', end = ' ')
    else:
        print(i, end = ' ')

    res[i] = res.get(i, 0) + 1