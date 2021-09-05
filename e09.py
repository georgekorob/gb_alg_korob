# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.


from random import randint
import numpy as np

size = 7
matrix = [[randint(0, 10) for _ in range(size)] for _ in range(size)]

print('Матрица: ')
for e in matrix:
    print(('{:5d}' * size).format(*e))

matrix = np.transpose(matrix)
print(f'Максимальный элемент среди минимальных: {max([min(e) for e in matrix])}')
