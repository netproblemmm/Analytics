# Задание 1: Поставьте оценку!
rating = -200
positiveRatingQty = 0
negativeRatingQty = 0

while rating != 0:
    rating = int(input("Введите рейтинг: "))
    if rating > 0:
        positiveRatingQty += 1
    if rating < 0:
        negativeRatingQty += 1

print("Кол-во положительных чисел: ", positiveRatingQty)
print("Кол-во отрицательных чисел: ", negativeRatingQty)
