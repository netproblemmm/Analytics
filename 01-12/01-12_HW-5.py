# Задача 5*. «Война и мир»
import os
import zipfile

os.chdir('D:/Projects/Analytics/01-12') 

with zipfile.ZipFile('01-12_HW-5_voyna-i-mir.zip', 'r') as zip_ref:
    file_name = [name for name in zip_ref.namelist() if name.endswith('.txt')][0]

    with zip_ref.open(file_name) as file:
        text = file.read().decode('utf-8')

char_count = {}

for char in text:
    if char.isalpha():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

sorted_chars = sorted(char_count.items(), key= lambda x: (-x[1], x[0]))

with open("01-12_HW-5_statistik.txt", "w", encoding="utf-8") as file:
    for char, freq in sorted_chars:
        file.write(f"{char}: {freq}\n")
        print(f"{char}: {freq}")