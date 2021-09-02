# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

year = input('Введите год: ')

if year.isdigit():
    year = int(year)
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        print(f"{year} - високосный год")
    else:
        print(f"{year} - невисокосный год")
else:
    print('Необходимо ввести число!')
