# Задание 1. Гласные буквы
text_string = input('Введите текст: ')
all_vowels = 'ауоыиэяюёе'
vowels = []

for i in text_string:
    if i in all_vowels:
        vowels.append(i)

# Можно также записать в виде генератора списка (List comprehension):
# vowels = [i for i in text_string if i in all_vowels]

print('Список гласных букв: ', vowels)
print('Длина списка: ', len(vowels))