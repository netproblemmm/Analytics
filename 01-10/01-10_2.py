# Выбрать только четные и составить список пар (число, квадрат числа)
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2)) # передаем в виде кортежа

# print(res)

# тоже самое, но в виде лямбда - функций
data = [1, 2, 3, 5, 8, 15, 23, 38]
def select(f, col):
    return[f(x) for x in col]

def where(f, col):
    return[x for x in col if f(x)]

res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x**2), res))
print(res)