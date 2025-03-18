# Задача 2. Обычный день на работе
hoursInWorkDay = 3
currentHour = 1
allTasksQty = 0
havingTalkWithWife = False

while currentHour <= hoursInWorkDay:
    print(currentHour, "- час")
    tasksQtyInHour = int(input("Сколько задач решит Максим? "))
    allTasksQty += tasksQtyInHour
    currentHour += 1
    if int(input("Звонит жена. Взять трубку? (1 - да, 0 - нет) ")) == 1:
        havingTalkWithWife = True

print("Рабочий день закончился. Всего выполнено задач: ", allTasksQty)
if havingTalkWithWife:
    print("Нужно зайти в магазин")