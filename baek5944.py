import sys
import heapq
sys.stdin = open("baek5944.txt")


def dijkstra(start, end):

    dist = [INF] * (P+1)
    dist[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))

    while hq:
        cost, node = heapq.heappop(hq)

        if dist[node] < cost:
            continue
        for next_node, next_cost in graph[node]:
            if dist[next_node] <= cost + next_cost:
                continue
            dist[next_node] = cost + next_cost
            heapq.heappush(hq, (dist[next_node], next_node))
    return dist[end]

INF = 98765432121
C, P, PB, PA1, PA2 = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(0, P+1)]
for i in range(0, C):
    s, e, c = map(int, sys.stdin.readline().split())
    graph[s].append((e, c))
    graph[e].append((s, c))

answer1 = dijkstra(PB, PA1) + dijkstra(PA1, PA2)
answer2 = dijkstra(PB, PA2) + dijkstra(PA2, PA1)

print(min(answer1, answer2))