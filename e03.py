# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.

from random import randint
from numpy import median


def median_search(lst, elem):
    if len(lst) == 1:
        return lst[0]
    pivot = lst[len(lst) // 2]
    left, pivots, right = [], 0, []
    for item in lst:
        if item < pivot:
            left += [item]
        elif item == pivot:
            pivots += 1
        else:
            right += [item]
    if elem < len(left):
        return median_search(left, elem)
    if elem < len(left) + pivots:
        return pivot
    else:
        return median_search(right, elem - len(left) - pivots)


m = 3
nums = [randint(0, m) for _ in range(m * 2 + 1)]
print(f'В массиве {nums} медиана: {median_search(nums, m)}')
print(f'Проверка сортированного массива {sorted(nums)} и его медианы {median(nums)}')

# В массиве [10, 12, 2, 6, 10, 14, 13] медиана: 10
# Проверка сортированного массива [2, 6, 10, 10, 12, 13, 14] и его медианы 10.0
