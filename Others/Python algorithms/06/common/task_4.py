# Created by Nikolay Pakhomov 26.02.2025
# Размер объекта в памяти.
import sys

print(sys.version, sys.platform)

a = 5
b = 124.54
c = 'Hello World!'

print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))
print()

lst = [i for i in range(10)]
print(sys.getsizeof(lst))


def show_size(x, level=0):
    print('\t' * level, f"type={x.__class__}, size={sys.getsizeof(x)}, object={x}")
    if hasattr(x, "__iter__"):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


show_size(a)
show_size(b)
show_size(c)
show_size(lst)

# кортеж
print('*' * 75)
t = tuple(lst)
show_size(t)

# множество - хэш таблица, занимает много памяти, однако предоставляет быстрый доступ к элементам.
print('*' * 75)
s = set(lst)
show_size(s)

# словарь
print('*' * 75)
d = {str(i): i for i in range(10)}
show_size(d)
