# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число; случайное вещественное число; случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

from random import random

r_start, r_end = input('Введите диапазон {start, end}: ').split()
if r_start.isdecimal():
    r_start, r_end = int(r_start), int(r_end)
    print(f'Случайная цифра: {int(random() * (r_end - r_start + 1)) + r_start}')
elif not r_start.isalpha():
    r_start, r_end = float(r_start), float(r_end)
    print(f'Случайное число: {random() * (r_end - r_start) + r_start}')
else:
    r_start, r_end = ord(r_start), ord(r_end)
    print(f'Случайный символ: {chr(int(random() * (r_end - r_start + 1)) + r_start)}')
