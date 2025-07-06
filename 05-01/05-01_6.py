# Lesson_01: Task_06

def calc(*args):
    sum_t = sum(args)
    kol_t = len(args)

    return {'sum': sum_t, 'mean': sum_t / kol_t}

print(calc(1, 85, 6, 2, 8, 6, 4))
