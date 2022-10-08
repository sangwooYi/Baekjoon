import sys
import heapq
sys.stdin = open("baek5972.txt")


def dijkstra(graph, n):
    INF = 987654321
    DP = [INF] * (n+1)
    DP[1] = 0

    hq = []
    heapq.heappush(hq, (0, 1))
    while hq:
        cost, node = heapq.heappop(hq)

        for next_node, next_cost in graph[node]:
            if DP[next_node] <= DP[node] + next_cost:
                continue
            DP[next_node] = DP[node] + next_cost
            heapq.heappush(hq, (DP[next_node], next_node))
    return DP[n]

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(0, N+1)]
for i in range(0, M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

answer = dijkstra(graph, N)
print(answer)