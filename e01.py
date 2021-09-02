# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number_read = input("Введите трехзначное число!")

if len(number_read) != 3 or not number_read.isdigit():
    print("Введите число из 3-х цифр!")
else:
    sum_d, prod_d = 0, 1
    for d in number_read:
        d = int(d)
        sum_d += d
        prod_d *= d
    print(f"Сумма цифр: {sum_d}\nПроизведение цифр {prod_d}")
