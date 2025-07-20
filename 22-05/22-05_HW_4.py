'''
4. Создайте функцию генератор чисел Фибоначчи
https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8
'''
def fibonacci(n: int):
  '''Генератор функции Фибоначчи.'''
  a, b = 0, 1
  yield a
  yield b
  for _ in range(n - 2):
    yield a + b
    a, b = b, a + b


n = int(input('Введите необходимое число чисел последовательности Фибоначчи: '))
list_fibonacci = [i for i in fibonacci(n)]
print(list_fibonacci)
