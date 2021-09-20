# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в
# виде функции. По возможности доработайте алгоритм (сделайте его умнее).

from random import randint
from timeit import timeit

SIZE = 20
COUNT_EXEC = 100000


def bubble_sort(lst):
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def bubble_sort_optimize(lst):
    for i in range(len(lst) - 1, 0, -1):
        is_sorted = True
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                is_sorted = False
        if is_sorted:
            break
    return lst


numbers = [randint(-100, 100) for _ in range(SIZE)]
print(numbers)
print(bubble_sort_optimize(numbers))
time_bubble_sort = timeit(f'bubble_sort({numbers})',
                          setup='from __main__ import bubble_sort',
                          number=COUNT_EXEC)
time_bubble_sort_optimize = timeit(f'bubble_sort_optimize({numbers})',
                                   setup='from __main__ import bubble_sort_optimize',
                                   number=COUNT_EXEC)
print(f'{time_bubble_sort} - время работы алгоритма сортировки пузырьком.')
print(f'{time_bubble_sort_optimize} - время работы оптимизированного алгоритма сортировки.')

# [-7, 66, -41, 81, 46, -59, 95, -51, -38, -70, -3, 97, 69, 52, 82, 23, 29, 98, -54, -93]
# [-93, -70, -59, -54, -51, -41, -38, -7, -3, 23, 29, 46, 52, 66, 69, 81, 82, 95, 97, 98]
# 2.1724962 - время работы алгоритма сортировки пузырьком.
# 0.2632880999999996 - время работы оптимизированного алгоритма сортировки.
# Время работы оптимизированного алгоритма значительно быстрее. При росте числа элементов массива разность во времени
# работы алгоритмов растет.
