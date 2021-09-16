# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
# уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность
# вашей ОС.

# lesson-3 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.

from random import randint
import sys
from time import time

MAXVALUE = 20


def sum_memory_test_1(lst, is_print=False):
    """Первая версия программы с использованием сортированного массива"""
    start = time()

    sorted_arr = sorted(lst)
    elements = sorted_arr[:2]

    finish = time()
    if is_print:
        print(f'Два наименьших элемента: {elements}')
    memory_sum = sys.getsizeof(lst) + sys.getsizeof(sorted_arr)
    memory_sum += sum(map(lambda x: sys.getsizeof(x), lst))
    memory_sum += sum(map(lambda x: sys.getsizeof(x), sorted_arr))
    memory_sum += sys.getsizeof(MAXVALUE)
    memory_sum += sys.getsizeof(elements)
    return memory_sum, finish-start


def sum_memory_test_2(lst, is_print=False):
    """Вторая версия программы с использованием двух хранимых переменных"""
    start = time()

    value_min_1 = min(lst)
    lst.remove(value_min_1)
    value_min_2 = min(lst)
    elements = [value_min_1, value_min_2]

    finish = time()
    if is_print:
        print(f'Два наименьших элемента: {elements}')
    memory_sum = sys.getsizeof(lst)
    memory_sum += sum(map(lambda x: sys.getsizeof(x), lst))
    memory_sum += sys.getsizeof(MAXVALUE)
    memory_sum += sys.getsizeof(value_min_1)
    memory_sum += sys.getsizeof(value_min_2)
    memory_sum += sys.getsizeof(elements)
    return memory_sum, finish-start


for size in [50000, 100000, 200000]:
    arr = [randint(0, MAXVALUE) for _ in range(size)]
    mem_sum_1, time_1 = sum_memory_test_1(arr)
    mem_sum_2, time_2 = sum_memory_test_2(arr)
    print(f'1 программа использует: {mem_sum_1} байт памяти для массива размером {size} и отрабатыет за {time_1:.1e}.')
    print(f'2 программа использует: {mem_sum_2} байт памяти для массива размером {size} и отрабатыет за {time_2:.1e}.')


# Версия Python 3.8.5
# ОС WindowsPE разрядность 64bit

# Вывод программы:
# 1 программа использует: 620 байт памяти для массива размером 5.
# 2 программа использует: 388 байт памяти для массива размером 5.
# 1 программа использует: 7556 байт памяти для массива размером 100.
# 2 программа использует: 3804 байт памяти для массива размером 100.
# 1 программа использует: 73892 байт памяти для массива размером 1000.
# 2 программа использует: 36976 байт памяти для массива размером 1000.

# Можно сделать вывод, что версия программы поиска наименьших элементов без сортировки массива использует
# намного меньше паняти, хотя массив можно было бы определить в ту же переменную lst, но создание нового массива
# и его сортировка всё равно бы была. Программа так же работает в 3-4 раза быстрее так как не надо тратить
# ресурсы на сортировку.
