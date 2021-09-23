# 2. Закодировать любую строку по алгоритму Хаффмана.
from collections import Counter, OrderedDict


class Haffman:
    class Node:
        """Узлы дерева."""
        def __init__(self, value, left=None, right=None):
            self.value = value  # Частота встречающегося элемента
            self.right = right  # Правый узел, исходящий из данного
            self.left = left  # Левый узел, исходящий из данного

        def __str__(self):
            return f'Node {self.value}:[{self.right} _ {self.left}]'

    class Leaf:
        """Конечные элементы дерева (символы)."""
        def __init__(self, key, value):
            self.key = key  # символ
            self.value = value  # код символа

        def __str__(self):
            return f'(leaf {self.key}:{self.value})'

    def __init__(self):
        self._table = dict()  # Словарь кодов для каждого символа
        self._tree = []  # Дерево элементов
        self._real_str = ''  # Кодируемая строка

    def _create_tree_and_table(self, real_str):
        """Создание дерева и словаря кодов символов."""
        self._real_str = real_str
        self._tree = []
        # Формируется упорядоченный словарь символов и их частот
        counter = OrderedDict(sorted(dict(Counter(self._real_str)).items(), key=lambda k: k[1], reverse=True))
        for key, value in counter.items():
            self._tree += [self.Leaf(key, value)]
        while len(self._tree) > 2:
            # Два самых редких элемента
            last_el, pre_last_el = self._tree.pop(), self._tree.pop()
            spam = self.Node(pre_last_el.value + last_el.value, pre_last_el, last_el)
            # Вставляем новый узел в соответствии с порядком по частоте
            if spam.value > self._tree[0].value:
                self._tree.insert(0, spam)
            elif spam.value <= self._tree[-1].value:
                self._tree.append(spam)
            else:
                for i in range(1, len(self._tree)):
                    if self._tree[i - 1].value >= spam.value > self._tree[i].value:
                        self._tree.insert(i, spam)
                        break
        # Создаем корень дерева, массив превращается в корневой узел
        self._tree = self.Node(self._tree[0].value + self._tree[1].value, self._tree[0], self._tree[1])
        self._create_table(self._tree)

    def _create_table(self, data, code=''):
        """Создание словаря кодов для каждого символа."""
        if isinstance(data, self.Node):
            # Код формируется прибавлением каждый раз 0 (если левее) или 1 (если правее)
            self._create_table(data.left, code=code + '0')
            self._create_table(data.right, code=code + '1')
        elif isinstance(data, self.Leaf):
            # Эта часть кода выполнится только когда достигнет листа или конечного элемента
            self._table[data.key] = code

    def encode(self, real_str):
        """Кодирование строки real_str в двоичный сжатый код."""
        self.__init__()
        self._create_tree_and_table(real_str)
        return ''.join([self._table[ch] for ch in self._real_str])

    def decode(self, code):
        """Декодировать из двоичного сжатого кода в строку."""
        decode_dict = {value: key for key, value in self._table.items()}
        real_str = []
        i = 0
        while i < len(code):
            j = i + 1
            # Находится последовательность 0 и 1 в коде, которая есть в словаре
            while code[i:j] not in decode_dict.keys():
                j += 1
            # Добавляется символ, соответствующий коду в словаре
            real_str += [decode_dict[code[i:j]]]
            i = j
        return ''.join(real_str)

    def get_table(self):
        """Вернуть таблицу."""
        return self._table

    def get_data(self):
        """Вернуть дерево."""
        return self._tree

    def get_real_str_code(self):
        """Полный двоичный код строки."""
        return ''.join([bin(ord(ch))[2:].zfill(8) for ch in self._real_str])


# my_string = input('Введите строку: ')
my_string = 'Tetta'
haf = Haffman()
encode_str = haf.encode(my_string)
decode_str = haf.decode(encode_str)
print(f'Введенная строка в двоичном виде: {haf.get_real_str_code()}')
print(f'Таблица для кодирования: {haf.get_table()}')
print(f'Строковое представление дерева: {haf.get_data()}')
print(f'Кодированная строка: {encode_str}')
print(f'Декодированная строка: {decode_str}')
print(f'Оригинальная строка: {my_string}')
print(f'Строки {"равны!" if decode_str == my_string else "не равны!"}')

# Введенная строка в двоичном виде: 0101010001100101011101000111010001100001
# Таблица для кодирования: {'e': '000', 'a': '001', 'T': '01', 't': '1'}
# Строковое представление дерева: Node 5:[(leaf t:2) _ Node 3:[(leaf T:1) _ Node 2:[(leaf a:1) _ (leaf e:1)]]]
# Кодированная строка: 0100011001
# Декодированная строка: Tetta
# Оригинальная строка: Tetta
# Строки равны!
