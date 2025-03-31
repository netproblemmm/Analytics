# Задание 1. Сумма чисел
import os

os.chdir('D:/Projects/Analytics/01-12') 

total_sum = 0

numbers_file = open('01-12_HW-1_numbers.txt', 'r', encoding='utf-8')

for line in numbers_file:
    numbers = [int(num) for num in line.split() if num]
    total_sum += sum(numbers)

numbers_file.close()

sum_file = open('answer.txt', 'w', encoding='utf-8')
sum_file.write(str(total_sum))
sum_file.close()