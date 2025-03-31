# Задача 4. Частотный анализ
import os
os.chdir('D:/Projects/Analytics/01-12') 

english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
total_letters = 0

with open('01-12_HW-4_text.txt', 'r') as text_file:
    text = text_file.read().lower()

letter_count = {letter: 0 for letter in english_alphabet}

for char in text:
    if char in english_alphabet:
        letter_count[char] += 1
        total_letters += 1

letter_freq = {letter: (count / total_letters) for letter, count in letter_count.items() if count > 0}
sorted_freq = sorted(letter_freq.items(), key=lambda x: (-x[1], x[0]))

with open('01-12_HW-4_analysis.txt', 'w') as write_file:
    for letter, freq in sorted_freq:
        write_file.write(f'{letter} {freq:.3f}\n')