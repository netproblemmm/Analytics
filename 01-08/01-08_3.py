# Задача 3. Простые числа
def prime(n):
    flag = True
    i = 2
    while i < n and flag:
        if n % i == 0:
            flag = False
        i += 1
    if flag:
        return 'Простое число'
    else:
        return 'Непростое число'

n = int(input())
print(prime(n))