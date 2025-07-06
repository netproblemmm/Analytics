# Lesson_01: HW_1

grades = [95, -10, 82, 90, -5, 77]

def normalize_grades(list):
    list_res = [i for i in list if i >= 0]
    return sorted(list_res, reverse=True)

print(normalize_grades(grades))
