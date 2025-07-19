'''
1. Напишите функцию для транспонирования матрицы
'''
def matrix_transpose(matrix: list[list]) -> list[list]:
    """Функция транспонирует матрицу"""

    new = []

    for i in range(len(matrix[0])):
        new.append([])
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new[j].append(matrix[i][j])
    return new        


matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix_transpose(matrix))
