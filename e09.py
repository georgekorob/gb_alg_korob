# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

nums = input('Введите три числа, через пробел: ').split()

if len(nums) != 3 or sum([n.isalpha() for n in nums]):
    print('Необходимо ввести 3 числа!')
else:
    n1, n2, n3 = [float(n) for n in nums]
    print('Среднее число ', end='')
    if n1 == n2 or n2 == n3 or n3 == n1:
        print('не существует из-за равенства!')
    elif n2 < n1 < n3 or n3 < n1 < n2:
        print(n1)
    elif n1 < n2 < n3 or n3 < n2 < n1:
        print(n2)
    else:
        print(n3)
