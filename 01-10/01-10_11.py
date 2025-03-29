# модуль os
import os

os.chdir('C:/Users/Hawk') # смена директория

print(os.getcwd()) # выдача текущего директория

print(os.path.basename('D:/Projects/Analytics/01-10/file.txt')) # базовое имя пути
# результат: file.txt

print(os.path.abspath('file.txt')) # абсолютное имя пути
# результат: D:/Projects/Analytics/01-10/file.txt