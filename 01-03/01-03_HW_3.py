# Задача 3. Игра «Угадай число»
guessNumber = 7
tryQty = 0

while True:
    number = int(input("Введите число: "))
    tryQty += 1
    if number == guessNumber:
        break
    if number < guessNumber:
        print("Число меньше, чем нужно. Попробуйте еще раз!")
    if number > guessNumber:
        print("Число больше, чем нужно. Попробуйте еще раз!")

print("Вы угадали!")
print("Попыток: ", tryQty)
