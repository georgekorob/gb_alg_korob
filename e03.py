# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


from random import randint

arr = [randint(0, 50) for _ in range(10)]
print(f'До подмены: {arr}')

mxi = arr.index(max(arr))
mni = arr.index(min(arr))

arr[mni], arr[mxi] = arr[mxi], arr[mni]
print(f'После подмены: {arr}')
