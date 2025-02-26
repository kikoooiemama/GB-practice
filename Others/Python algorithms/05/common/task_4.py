# Created by Nikolay Pakhomov 12.02.2025
# OrderDict. OrderDict запоминает порядок, в котором были добавлены "ключи".

from collections import OrderedDict

a = {'cat': 5, 'dog': 2, 'mouse': 4}
print(a)
new_a = OrderedDict(sorted(a.items(), key=lambda x: x[0]))
print(new_a)

print()
b = {'cat': 5, 'dog': 2, 'mouse': 4}
print(b)
new_b = OrderedDict(sorted(a.items(), key=lambda x: x[1]))
print(new_b)
print(new_b == new_a)

print()
print(new_b)
new_b.move_to_end('mouse', last=False)
print(new_b)

new_b.popitem(False)
print(new_b)

new_b['cow'] = 1
print(new_b)

new_b['dog'] = 8
print(new_b)

print()
print("*" * 50)
new_c = OrderedDict(sorted(a.items(), key=lambda x: len(x[0])))
print(new_c)

for key in reversed(new_c):
    print(key, new_c[key])

# Профильтровать ip-адреса
from collections import OrderedDict, defaultdict, deque

N = 3000
with open('log.txt', 'r', encoding='utf-8') as f:
    log = deque(f, N)

print(log)

data = OrderedDict()
spam = defaultdict(int)

for item in log:
    ip = item[:-1]

    if not ip.startswith("192.168"):
        spam[ip] += 1
        data[ip] = 1

print(spam)
print(data)

data.update(spam)
print(data)

with open('data.txt', 'w', encoding='utf-8') as f:
    for key, value in data.items():
        f.write(f'{key} - {value}\n')
