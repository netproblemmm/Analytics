#Задание 1: Язык математики
print('Задание 1: Язык математики')

a = 8
b = 10
c = 12
d = 18

res = ((-3 + a**2) * b - 2**3) / (c - 2 * d)
print (res)
print ()

#Задание 2: Часы
print('Задание 2: Часы')

minutes = int(input('Введите к-во минут: '))

hours = minutes // 60
rest_minutes = minutes % 60

print('Это ', hours, ' часов и ', rest_minutes, ' минут')
print ()

#Задание 3: Счастливый билет
print('Задание 3: Счастливый билет')

number = int(input('Введите номер билета: '))
#number = int(834762)

number1 = number // 100000
number2 = number // 10000 % 10
number3 = number // 1000 % 10
number4 = number // 100 % 10
number5 = number // 10 % 10
number6 = number % 10
print(number1,number2,number3,number4,number5,number6)

if number1 + number2 + number3 == number4 + number5 + number6:
    print('Yes')
else:
    print('No')
print ()


#Задание 4: Площадь прямоугольного треугольника
print('Задание 4: Площадь прямоугольного треугольника')

a = int(input('Введите длину 1 катета: '))
b = int(input('Введите длину 2 катета: '))

square = int((a * b) / 2)
print('Площадь прямоугольного треугольника: ', square)

#Задание 5: Поменять местами
print('Задание 5: Поменять местами')

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)
a = a + b
b = a - b
a = a - b
print(a, b)