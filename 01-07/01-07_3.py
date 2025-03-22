# Импорт функции
import modul1
print(modul1.max1(5, 9))

# Импорт конретной функции
from modul1 import max1
print(max1(5, 9))

# Импорт всех функций
from modul1 import *
print(max1(5, 9))

# Использование псевдонима названия модуля
import modul1 as m1
print(m1.max1(5, 9))