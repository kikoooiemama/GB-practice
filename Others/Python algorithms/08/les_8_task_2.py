# Created by Nikolay Pakhomov 24.03.2025
# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он
# дополнительно возвращал список вершин, которые необходимо обойти.
from collections import deque

g = [
    [0, 0, 1, 1, 9, 0, 0, 0, ],
    [0, 0, 9, 4, 0, 0, 5, 0, ],
    [0, 9, 0, 0, 3, 0, 6, 0, ],
    [0, 0, 0, 0, 0, 0, 0, 0, ],
    [0, 0, 0, 0, 0, 0, 1, 0, ],
    [0, 0, 0, 0, 0, 0, 5, 0, ],
    [0, 0, 7, 0, 8, 1, 0, 0, ],
    [0, 0, 0, 0, 0, 1, 2, 0, ],
]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                new_cost = vertex + cost[start]
                if cost[i] > new_cost:
                    cost[i] = new_cost
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    track = {}
    for i, vertex in enumerate(parent):
        if vertex > -1:
            track[i] = deque([vertex, i])

            while vertex > -1:
                vertex = parent[vertex]
                if vertex > -1:
                    track[i].appendleft(vertex)

            track[i] = list(track[i])

    return track


print(dijkstra(g, 0))
