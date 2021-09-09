# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых
# трёх уроков. Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
# 2.4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125


import time
import unittest
import sys


sys.setrecursionlimit(4000)


# Метод обычного перебора работает быстро O(n)
def sum_numbers_range_1(count_numbers):
    sum_numbers, current_number = 0, 1
    for cn in range(count_numbers):
        sum_numbers += current_number
        current_number /= -2
    return sum_numbers


# Рекурсивный метод работает намного дольше, хотя тоже должен быть O(n)
def sum_numbers_range_2(count_numbers, current_number=1.):
    if count_numbers == 0:
        return 0
    else:
        return current_number + sum_numbers_range_2(count_numbers - 1, -current_number / 2)


class SumNumbersTest(unittest.TestCase):
    def _test_time_taken(self, my_func, n=2000):
        self.assertEqual(0, 0)  # Чтобы pycharm не ругался на method may be static
        start = time.time()
        my_func(n)
        finish = time.time()
        print(f'Время работы функции {my_func.__name__} для {n} чисел: {finish-start:.6f}')

    def _test_functional(self, my_func):
        self.assertEqual(0.5, my_func(2))
        self.assertEqual(0.75, my_func(3))
        self.assertEqual(0.625, my_func(4))
        self.assertEqual(0.6875, my_func(5))
        self.assertEqual(0.65625, my_func(6))

    def test_func_01(self):
        self._test_time_taken(sum_numbers_range_1)
        self._test_functional(sum_numbers_range_1)
        print()

    def test_func_02(self):
        self._test_time_taken(sum_numbers_range_2)
        self._test_functional(sum_numbers_range_2)
        print()


if __name__ == '__main__':
    unittest.main()
