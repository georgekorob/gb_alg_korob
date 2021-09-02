# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

letters = [x.lower() for x in input('Введите две буквы от a - Z: ').split()]
poss = [ord(letter)-ord("a")+1 for letter in letters]

for l, p in zip(letters, poss):
    print(f'Буква {l} на позиции: {p}')

print(f'Между этими буквами находится ещё {poss[1]-poss[0]-1}!')
