# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.


from random import randint

arr = [randint(-20, 20) for _ in range(10)]
print(f'Массив: {arr}')

mni = arr.index(min(arr))
mxi = arr.index(max(arr))
if mni > mxi:
    mni, mxi = mxi, mni

sum_arr_ind = sum(arr[mni+1:mxi])
print(f'Сумма элементов между минимальным и максимальным элементами = {sum_arr_ind}')
