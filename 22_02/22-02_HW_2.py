# 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def convert_in_hex(num: int) -> str:
    hex_characters = "0123456789ABCDEF"
    if num == 0:
        return "0"
    
    hex_number = ""
    while num > 0:
        remainder = num % 16
        hex_number = hex_characters[remainder] + hex_number
        num //= 16
    return hex_number

number = int(input("Введите число: "))
print(convert_in_hex(number))
print(f"Проверочная функция hex = {hex(number)}")
