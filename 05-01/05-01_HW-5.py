# Lesson_01: HW_5

employees = [("Alice", 30), ("Bob", -5), ("Charlie", 40)]

def average_age(list) -> int:
    valid_ages = [age for name, age in employees if age >= 0]

    return sum(valid_ages) / len(valid_ages)

print(average_age(employees))