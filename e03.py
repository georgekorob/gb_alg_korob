# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, то надо вывести число 6843.


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

    print(f'Число {number} в обратном порядке будет {number[::-1]}')
