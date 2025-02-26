# Created by Nikolay Pakhomov 12.02.2025
# Deque

from collections import deque

a = deque()
b = deque('asdjhdfg')
c = deque([1, 2, 3, 4, 5])
print(a, b, c, sep='\n')

print("*" * 50)

b = deque('asdjhdfg', maxlen=3)
c = deque([1, 2, 3, 4, 5], maxlen=4)
print(b, c, sep='\n')

print("*" * 50)
c.clear()
print(b, c, sep='\n')

print("*" * 50)
d = deque([i for i in range(5)])
print(d)
d.append(5)
d.appendleft(6)
print(d)
d.extend([7, 8, 9])
d.extendleft([10, 11, 12])
print(d)

print("*" * 50)
d = deque([i for i in range(5)], maxlen=6)
print(d)
d.append(5)
d.appendleft(6)
print(d)
d.extend([7, 8, 9])
d.extendleft([10, 11, 12])
print(d)

print("*" * 50)
f = deque([i for i in range(5)], maxlen=7)
x = f.pop()
y = f.popleft()
print(f, x, y, sep='\n')

print("*" * 50)
g = deque([i for i in range(5)], maxlen=7)
print(g)
print(g.count(2))
print(g.index(3))
g.insert(2, 6)  # добавили по индексу в дек
print(g)

g.reverse()
print(g)

g.rotate(3)
print(g)

print("*" * 50)
import random

array = [random.randint(-100, 100) for _ in range(10)]
print(array)

deq = deque()

for item in array:
    if item > 0:
        deq.append(item)
    else:
        deq.appendleft(item)
print(deq)

print("*" * 50)
with open('log.txt', 'r', encoding='utf-8') as f:
    last_ten = deque(f, 10)
print(last_ten)
