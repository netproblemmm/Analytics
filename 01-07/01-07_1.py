def sum_numbers(n, y = 'Hello'):
    print(y)
    summma = 0
    for i in range(1, n + 1):
        summma += i
    return summma

a = sum_numbers(5, 'qwert')
print(a)
