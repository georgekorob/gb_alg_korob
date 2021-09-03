# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых
# чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.


while True:
    u_number = input('Последовательность чисел: ')
    u_number = u_number.strip()
    if not u_number.isdigit():
        print('Нужно ввести именно число!')
        continue
    elif u_number == '0':
        break
    u_digit = input('Цифра: ')
    u_digit = u_digit.strip()
    if not u_digit.isdigit() and len(u_digit) != 1:
        print('Нужно ввести именно цифру!')

    count = sum([u_digit == n for n in u_number])
    print(f'Цифра {u_digit} встречается в {u_number} всего {count} раз')
