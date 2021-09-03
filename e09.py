# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и
# сумму его цифр.


numbers = input('Введите натуральные числа: ').split()
sum_numbers = [sum([int(n) for n in number]) for number in numbers]
index_of_max = sum_numbers.index(max(sum_numbers))

print(f'Число {numbers[index_of_max]} имеет наибольшую сумму цифр, равную {sum_numbers[index_of_max]}')
