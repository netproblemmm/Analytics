# Задача 5. Пропавшая карточка
cardsSum = 0

cardsQty = int(input("Введите число карточек: "))
for card in range(1, cardsQty + 1):
    cardsSum += card

print("Сумма карточек равна: ", cardsSum)

for card in range (cardsQty - 1):
    cardsSum -= int(input("Введите номер оставшейся карточки: "))

print("Номер потерянной карточки: ", cardsSum)

# Но задачу лучше решить через массивы,
# так как юзер может дважды ввести один и тот же номер оставшейся карточки