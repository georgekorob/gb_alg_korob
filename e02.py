# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3
# четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


# numbers_str = ['0', '34560', '897324', 't7y4834', 'ggudftuj', ' 34562']


# while numbers_str:
while True:
    # number = numbers_str.pop()
    # print(number, end='\t')
    number = input('Введите число: ')
    number = number.strip()
    if not number.isdigit():
        print('Нужно ввести именно число!')
        continue
    elif number == '0':
        break

    even = odd = 0
    for n in number:
        if int(n) % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f'Число {number} имеет {even} четных цифр и {odd} нечетных цифр.')
