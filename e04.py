# 4. Определить, какое число в массиве встречается чаще всего.


from random import randint

arr = [randint(0, 3) for _ in range(10)]
print(f'Массив: {arr}')
arr_set = list(set(arr))
counts = [arr.count(n) for n in arr_set]
mxi = arr_set[counts.index(max(counts))]

print(f'Число {arr_set[mxi]} встречается {counts[mxi]} раз')
