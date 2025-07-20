# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

from math import gcd
from fractions import Fraction

fraction1 = '1/2'
fraction2 = '4/6'

numerator_1, denominator_1 = map(int, fraction1.split('/'))
numerator_2, denominator_2 = map(int, fraction2.split('/'))

def fractions_sum(n1, d1, n2, d2: int):
    if d1 == d2:
        print(f'Сумма дробей - {n1 + n2}/{d2}')
    else:
        cd = int(d1 * d2 / gcd(d1, d2))
        rn = int(cd / d1 * n1 + cd / d2 * n2)
        g2 = gcd(rn, cd)
        n = int(rn / g2)
        d = int(cd / g2)
        print(f'Сумма дробей - {n}/{d}' if n != d else n)

def fractions_multiply(n1, d1, n2, d2: int):
    n = n1 * n2
    d = d1 * d2
    divisor = gcd(n, d)
    n //= divisor
    d //= divisor
    print(f'Произведение дробей - {n}/{d}')

fractions_sum(numerator_1, denominator_1, numerator_2, denominator_2)
fractions_multiply(numerator_1, denominator_1, numerator_2, denominator_2)

# Проверка с помощью функции Fraction

print("Проверка функцией Fraction: ")
print(f'Сумма дробей - {Fraction(fraction1) + Fraction(fraction2)}')
print(f'Произведение дробей - {Fraction(fraction1) * Fraction(fraction2)}')
