# Created by Nikolay Pakhomov 12.02.2025
# ChainMap - цепочка отображений, для работы с несколькими словарями. Поиск ключа происходит последовательно в каждом
# словаре цепочки

from collections import ChainMap
import argparse

d_1 = {'a': 2, 'b': 4, 'c': 6}
d_2 = {'a': 10, 'b': 20, 'd': 40}

d_map = ChainMap(d_1, d_2)
print(d_map)
d_2['a'] = 100
print(d_map)

print(d_map['a'])
print(d_map['d'])

print("*" * 50)
x = d_map.new_child()
print(x)

print(x.maps[0])
print(x.maps[-1])

print(x.parents)

print("*" * 50)
y = d_map.new_child()
print(y)
print(y['a'])

y['a'] = 1
print(y)

print(list(y))
print(list(y.values()))

defaults = {"ip": "localhost", "port": 7777}

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--ip")
parser.add_argument("-p", "--port")

args = parser.parse_args()
new_dict = {key: value for key, value in vars(args).items() if value}

settings = ChainMap(new_dict, defaults)
print(settings['ip'])
print(settings['port'])
