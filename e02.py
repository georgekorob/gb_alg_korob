# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.


import time
import unittest
import math


def sieve_without_eratosthenes(index_of_number):
    """Поиск i-го простого числа без использования алгоритма «Решето Эратосфена»"""

    number = 2
    primes = [number]
    while len(primes) < index_of_number:
        number += 1
        primes += [number]
        for j in primes[:-1]:
            if number % j == 0:
                primes.pop()
                break
    return primes[-1]


def sieve_eratosthenes(index_of_number):
    """Поиск i-го простого числа, используя алгоритм «Решето Эратосфена»"""

    size_for_prime = index_of_number + 1
    while index_of_number >= int(size_for_prime/math.log(size_for_prime)):
        size_for_prime += 1
    numbers = set(range(2, size_for_prime))
    primes = []

    while len(primes) < index_of_number and numbers:
        primes += [min(numbers)]
        numbers -= set(range(primes[-1], size_for_prime, primes[-1]))
    if primes:
        return primes[-1]
    else:
        return 2


# Время работы функций для простого числа (под номером / sieve_without_eratosthenes / sieve_eratosthenes):
# 100 / 0.000997 / 0.001002
# 500 / 0.018996 / 0.013001
# 1000 / 0.076003 / 0.033997
# 2000 / 0.284021 / 0.234007
# 5000 / 1.762979 / 0.831023
# Можно сделать вывод, что метод решето Эратосфена стабильно ускоряет нахождение прочтого числа
# Сложность алгоритма составляет O(n*log(n)) линеарифметическая
# А без Эратосфена сложность O(n**2)


class SumNumbersTest(unittest.TestCase):
    def _test_time_taken(self, my_func, n=1000):
        self.assertEqual(0, 0)  # Чтобы pycharm не ругался на method may be static
        start = time.time()
        my_func(n)
        finish = time.time()
        print(f'Время работы функции {my_func.__name__}: {finish-start:.6f}')

    def _test_functional(self, my_func):
        self.assertEqual(2, my_func(1))
        self.assertEqual(5, my_func(3))
        self.assertEqual(11, my_func(5))
        self.assertEqual(17, my_func(7))
        self.assertEqual(29, my_func(10))

    def test_func_01(self):
        self._test_time_taken(sieve_without_eratosthenes)
        self._test_functional(sieve_without_eratosthenes)
        print()

    def test_func_02(self):
        self._test_time_taken(sieve_eratosthenes)
        self._test_functional(sieve_eratosthenes)
        print()


if __name__ == '__main__':
    unittest.main()
