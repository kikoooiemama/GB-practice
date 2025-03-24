# Created by Nikolay Pakhomov 24.03.2025
from collections import deque

# Поиск кратчайшего пути
# 1. Вершину помещаем в пустую очередь
# 2. Извлечь из начала очереди вершину:
# a) Если вершина является целевой, то завершить поиск
# б) В противном случае, в конец очереди добавляются все смежные вершины, которые еще не пройдены и не находятся в
# очереди.
# 3. Если очередь пуста, то все вершины графа были просмотрены, значит пути нет, поиск завершен

g = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
]


def bfs(graph, start, finish):
    parent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]

    deq = deque([start])
    is_visited[start] = True

    while len(deq) > 0:
        current = deq.pop()
        if current == finish:
            # return parent
            break

        for i, vertex in enumerate(graph[current]):
            if vertex == 1 and not is_visited[i]:
                is_visited[i] = True
                parent[i] = current
                deq.appendleft(i)

    else:
        return f"Из вершины {start} нельзя попасть в вершину {finish}"
    cost = 0
    way = deque([finish])
    i = finish

    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]

    cost += 1
    way.appendleft(start)

    return f"кратчайший путь {list(way)} длинною в {cost} условных единиц"


s = int(input("От какой вершины идти: "))
f = int(input("До какой вершины идти: "))
print(bfs(g, s, f))
