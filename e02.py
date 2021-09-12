# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections

from collections import deque

# Создание словаря преобразования десятичного числового значения в шестнадцатиричное строковое представление
dic_nums = {i: v for i, v in enumerate([str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F'])}
dic_nums = {**{v: i for i, v in dic_nums.items()}, **dic_nums}

# strings_input = ['A2', 'C4F']
strings_input = [input(f'{n} число: ').upper() for n in range(1, 3)]
dic_ff = {str_i: list(str_i) for str_i in strings_input}
print(dic_ff)


def ff_int(x):
    """Функция для преобразования шестнадцатиричной строки в десятичное число"""
    x = deque(reversed(x))
    return sum([dic_nums[c] * (16 ** i) for i, c in enumerate(x)])


def int_ff(x):
    """Функция для преобразования десятичного числа в шестнадцатиричную строку"""
    y = deque()
    while x:
        y.appendleft(dic_nums[x % 16])
        x = x // 16
    return ''.join(list(y))


# Сложение и умножение методами преобразование в десятичный вид
result_sum1 = int_ff(ff_int(strings_input[0]) + ff_int(strings_input[1]))
result_mul1 = int_ff(ff_int(strings_input[0]) * ff_int(strings_input[1]))
print(f'Метод с преобразованием: {result_sum1}, {result_mul1}')

# Сложение и умножение встроенными методами
result_sum2 = (str(hex(int(strings_input[0], 16) + int(strings_input[1], 16)))[2:]).upper()
result_mul2 = (str(hex(int(strings_input[0], 16) * int(strings_input[1], 16)))[2:]).upper()
print(f'Самый простой метод: {result_sum2}, {result_mul2}')

# Вывод
# {'A2': ['A', '2'], 'C4F': ['C', '4', 'F']}
# Метод с преобразованием: CF1, 7C9FE
# Самый простой метод: CF1, 7C9FE
