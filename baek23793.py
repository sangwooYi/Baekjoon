import sys
import heapq
sys.stdin = open("baek23793.txt")

"""
방향성 그래프!

1) Y 거쳐서 Z도달 dijkstra(start, Y) + dijkstra(Y, end)
2) Y 안거치고 Z 도달 dijkstra(start, end) 인데, 다음 노드가 Y이면  pass하는 로직
"""


def dijkstra_normal(start, end):
    dist = [INF] * (N+1)

    dist[start] = 0
    hq = []

    heapq.heappush(hq, (0, start))

    while hq:
        cost, node = heapq.heappop(hq)

        if dist[node] < cost:
            continue

        for next_node, next_cost in graph[node]:
            if dist[next_node] <= cost+next_cost:
                continue
            dist[next_node] = cost+next_cost
            heapq.heappush(hq, (dist[next_node], next_node))
    return dist[end]

def dijkstra_nodepass(start, end, pass_node):
    dist = [INF] * (N+1)

    dist[start] = 0
    hq = []

    heapq.heappush(hq, (0, start))

    while hq:
        cost, node = heapq.heappop(hq)

        if dist[node] < cost:
            continue

        for next_node, next_cost in graph[node]:
            if next_node == pass_node:
                continue
            if dist[next_node] <= cost+next_cost:
                continue
            dist[next_node] = cost+next_cost
            heapq.heappush(hq, (dist[next_node], next_node))
    return dist[end]

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(0, N+1)]

INF = 98765432121

for i in range(0, M):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

X, Y, Z = map(int, sys.stdin.readline().split())

answer1 = dijkstra_normal(X, Y) + dijkstra_normal(Y, Z)
if answer1 >= INF:
    answer1 = -1
answer2 = dijkstra_nodepass(X, Z, Y)
if answer2 >= INF:
    answer2 = -1

print(answer1, answer2)
