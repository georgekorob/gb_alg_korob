# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с
# клавиатуры.


while True:
    n = input('Введите количество элементов n, сумму которых надо посчитать: ')
    n = n.strip()
    if not n.isdigit():
        print('Нужно ввести именно число!')
        continue
    elif n == '0':
        break

    count = int(n)-1
    range_number = sum_n = 1
    while count:
        range_number /= -2
        sum_n += range_number
        count -= 1
    print(f'Сумма {n} элементов равна {sum_n}')
