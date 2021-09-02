# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

char_number = input('Введите порядковый номер буквы в алфавите: ')

if char_number.isdigit() and 0 < int(char_number) < 27:
    print(f'Буква под номером {char_number}: {chr(int(char_number) + ord("a") - 1)}')
else:
    print(f'Порядковый номер должен быть числом от 1 до 26 включительно!')
