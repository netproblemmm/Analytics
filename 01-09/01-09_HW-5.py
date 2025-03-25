# Задача 5. Шифр Цезаря
# Определение русского алфавита, включая букву 'ё'
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

# Функция для шифрования текста по методу Цезаря
def caesar_cipher(string, user_shift):
    char_list = []
    # Создание списка зашифрованных символов
    for symb in string:
        if symb in alphabet:
            char_list.append(alphabet[(alphabet.index(symb) + user_shift) % len(alphabet)])
        else:
            char_list.append(symb)
    return ''.join(char_list)

# Функция, выраженная посредством генератора списков (в данном случае падает читаемость кода)
# def caesar_cipher(string, user_shift):
#     # Создание списка зашифрованных символов
#     char_list = [(alphabet[(alphabet.index(symb) + user_shift) % len(alphabet)]
#     if symb in alphabet else symb)
#     for symb in string]
#     # Преобразование списка символов в строку
#     new_str = ''.join(char_list)
#     return new_str

# Ввод пользователем исходного сообщения и сдвига
input_str = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

# Шифрование сообщения
output_str = caesar_cipher(input_str, shift)
# Вывод зашифрованного сообщения
print('Зашифрованное сообщение:', output_str)