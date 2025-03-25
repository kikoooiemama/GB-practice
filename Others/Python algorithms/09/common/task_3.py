# Created by Nikolay Pakhomov 25.03.2025
import hashlib

# Хеш-функции предназначены для "сжатия" произвольного сообщения или набора данных, записанных в двоичном алфавите,
# в битовую комбинацию фиксированной длины - свертку.
# dict/set

h_list = [None] * 26


def my_append(value):
    index = ord(value[0]) - ord('a')
    h_list[index] = value
    print(h_list)


a = 'apricot'
my_append(a)

b = 'banana'
my_append(b)

c = 'apple'
my_append(c)

print(4625 == 4 * 10 ** 3 + 6 * 10 ** 2 + 2 * 10 + 5)


def my_index(value):
    letter = 26
    index = 0
    size = 10000

    for i, char in enumerate(value):
        index += (ord(char) - ord('a') + 1) * letter ** i

    return index % size


print(my_index(a))
print(my_index(b))
print(my_index(c))
print("*" * 85)

# Хеширование
print(hashlib.sha1(b'Hello World!').hexdigest())
print(hashlib.sha1(b'Hello World.').hexdigest())
print(hashlib.sha1(b'kjsdhfk' + b'Hello World').hexdigest())

s = hashlib.sha1(b'Hello World').hexdigest()

print(s.encode('utf-8'))
print(hashlib.sha1(b'dfewertr' + bytes(s.encode('utf-8'))).hexdigest())
