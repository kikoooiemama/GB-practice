# Created by Nikolay Pakhomov 27.02.2025
# Структура объекта в памяти.
import sys
import ctypes
import struct

a = 5
b = 124.54
c = 'Hello World!'

# адрес объекта в памяти
print(id(a))
print(sys.getsizeof(a))

print(ctypes.string_at(id(a), sys.getsizeof(a)))
print(struct.unpack("LLLLLLl", ctypes.string_at(id(a), sys.getsizeof(a))))

print("*" * 50)
a = 59
x = y = a
print(id(a))
print(sys.getsizeof(a))

print(ctypes.string_at(id(a), sys.getsizeof(a)))
print(struct.unpack("LLLLLLl", ctypes.string_at(id(a), sys.getsizeof(a))))
print(id(int))

print("*" * 50)
print(id(b))
print(sys.getsizeof(b))

print(ctypes.string_at(id(b), sys.getsizeof(b)))
print(struct.unpack("LLLd", ctypes.string_at(id(b), sys.getsizeof(b))))
print(id(float))

print("*" * 50)
print(id(c))
print(sys.getsizeof(c))

print(ctypes.string_at(id(c), sys.getsizeof(c)))
print(struct.unpack("LLLLLLLLli" + 'c' * 13, ctypes.string_at(id(c), sys.getsizeof(c))))

print("*" * 50)
lst = [1, 2, 3, 4]
print(struct.unpack('LL' + 'L' * 5 * 4, ctypes.string_at(id(lst), sys.getsizeof(lst))))
