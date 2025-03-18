# Задача 4. Посчитай чужую зарплату...
monthQty = 3
currentMonth = 1
salaryYear = 0

while currentMonth <= monthQty:
    salaryMonth = int(input("Введите зарплату за " + str(currentMonth) + " месяц: "))
    currentMonth += 1
    salaryYear += salaryMonth

print("Средняя зарплата за месяц: ", int(salaryYear / monthQty))
