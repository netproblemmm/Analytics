# Функции
def calc1(a, b):
    return a + b

#calc1 = lambda a, b: a + b
# Запись лямбда-функции (сокращает код)

def calc2(a, b):
    return a * b

def math(op, x, y):
    print(op(x, y))

# Можно передать в функцию math - другую функцию calc1 + ее аргументы отдельно.
# В функции math - будет корректно вычислена функция calc1 с аргументами,
# несмотря на то, что после названия функции аргументы не были указаны (как calc1(5, 45))
math(calc1, 5, 45)