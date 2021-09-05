# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.


from random import randint

# Основной массив
arr = [randint(-20, 20) for _ in range(20)]
print(f'Массив: {arr}')

# Массив всех отрицательных чисел и их индексов в основном массиве
negative = [[i, n] for i, n in enumerate(arr) if n < 0]
# Массив индексов отрицательных чисел в основном массиве
neg_ind = [e[0] for e in negative]
# Массив значений отрицательных чисел
neg_val = [e[1] for e in negative]
# Индекс максимального отрицательного числа в основном массиве
neg_ind_in_all = neg_ind[neg_val.index(max(neg_val))]
print(f'Максимальный отрицательный элемент: {arr[neg_ind_in_all]}')
