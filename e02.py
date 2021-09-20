# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import uniform

SIZE = 12


def merge_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        mid = len(lst) // 2
        left, right, result = merge_sort(lst[:mid]), merge_sort(lst[mid:]), []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result += [left[i]]
                i += 1
            else:
                result += [right[j]]
                j += 1
        result += left[i:] + right[j:]
        return result


numbers = [uniform(0, 50) for _ in range(SIZE)]
print('Массив:\t\t\t\t', ('{:.2f}\t' * SIZE).format(*numbers))
print('После сортировки:\t', ('{:.2f}\t' * SIZE).format(*merge_sort(numbers)))

# Массив:			17.20	21.86	30.64	13.80	20.34	8.14	23.94	20.30	43.43	20.53	6.21	3.74
# После сортировки:	 3.74	6.21	8.14	13.80	17.20	20.30	20.34	20.53	21.86	23.94	30.64	43.43
