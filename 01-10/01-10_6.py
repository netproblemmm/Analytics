# тоже самое, но с сокращением кода, за счет использования функций map и filter
data = [1, 2, 3, 5, 8, 15, 23, 38]

res = map(int, data)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x**2), res))
print(res)