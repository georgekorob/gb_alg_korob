# 1. Определить количество различных подстрок с использованием хеш-функции. Задача: на вход функции дана строка,
# требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

import hashlib

str_input = 'Какая-то строка...'
substrings = set()

for i in range(len(str_input)):
    for j in range(len(str_input), i, -1):
        str_hash = hashlib.sha1(str_input[i:j].encode('utf-8')).hexdigest()
        # print(str_input[i:j], str_hash)
        substrings.add(str_hash)

print(f'В строке {str_input} {len(substrings) - 1} различных подстрок')

# В строке Какая-то строка... 161 различных подстрок
