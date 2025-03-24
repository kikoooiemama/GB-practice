# Created by Nikolay Pakhomov 19.07.2024
# 1. На улице встретились N друзей. Каждый пожал руку всем
# остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

s = int(input("Введите количество друзей жмущих руку друг другу: "))

graph = []
for i in range(s):
    row = [1] * s
    row[i] = 0
    graph.append(row)

print(graph)

handshakes = 0
for row in graph:
    for i in row:
        handshakes += i

handshakes //= 2

print(f"Всего было произведено {handshakes} рукопожатя(ий)")
