# Created by Nikolay Pakhomov 12.02.2025
# Defaultdict

from collections import defaultdict

a = defaultdict()
print(a)

s = 'flhklhlkfhjkljsdl;fjs;lfjs;lfj;sf'
b = defaultdict(int)

for i in s:
    b[i] += 1

print(b)

list_1 = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 1), ('dog', 1)]
c = defaultdict(list)
for k, v in list_1:
    c[k].append(v)
print(c)

list_1 = [('cat', 1), ('dog', 5), ('cat', 2), ('mouse', 1), ('dog', 1)]
d = defaultdict(set)
for k, v in list_1:
    d[k].add(v)
print(d)
