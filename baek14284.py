import sys
import heapq
sys.stdin = open("baek14284.txt")


def dijkstra(start, end):
    INF = 9876544321
    dist = [INF] * (N+1)

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
            dist[next_node] = cost+next_cost
            heapq.heappush(hq, (dist[next_node], next_node))
    return dist[end]

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(0, N+1)]

for i in range (0, M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

s, t = map(int, sys.stdin.readline().split())
answer = dijkstra(s, t)
print(answer)