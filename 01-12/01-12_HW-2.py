# Задание 2. Текст наоборот
import os

os.chdir('D:/Projects/Analytics/01-12') 

zen_file = open('01-12_HW-2_zen.txt', 'r')
data = zen_file.readlines()
zen_file.close()

for line in reversed(data):
    print(line.strip())