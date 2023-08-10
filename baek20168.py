import sys
sys.stdin = open("baek20168.txt")
import heapq

# N : 교차로 갯수  
N, M, A, B, C = map(int, input().split())
graph = [[] for _ in range(0, N+1)]

for i in range(0, M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

INF = 9876543211
dist = [INF] * (N+1)

hq = []
dist[A] = 0
heapq.heappush(hq, (0, 0, A))

while hq:

    cost, total, node = heapq.heappop(hq)

    if cost > dist[node]:
        continue
    if total > C:
        continue
    for next_node, next_cost in graph[node]:
        next_num = max(cost, next_cost)
        next_total = total+next_cost
        if dist[next_node] <= next_num:
            continue
        if next_total > C:
            continue
        dist[next_node] = next_num
        heapq.heappush(hq, (next_num, next_total, next_node))

answer = dist[B]
if answer == INF:
    answer = -1
print(answer)