import sys
import heapq
sys.stdin = open("baek17396.txt")


def dijkstra():

    INF = 9999999999
    dist = [INF] * N

    hq = []
    dist[0] = 0
    heapq.heappush(hq, (0, 0))

    while hq:
        cost, node = heapq.heappop(hq)

        if dist[node] < cost:
            continue

        for next_node, next_cost in graph[node]:
            if dist[next_node] <= cost + next_cost:
                continue
            # N-2 이전까지는 보이는곳을 못감
            if next_node < N-1 and is_sight[next_node]:
                continue
            dist[next_node] = cost+next_cost
            heapq.heappush(hq, (dist[next_node], next_node))
    
    if dist[N-1] == INF:
        res = -1
    else:
        res = dist[N-1]
    return res


N, M = map(int, sys.stdin.readline().split())
is_sight = list(map(int, sys.stdin.readline().split()))
# 0 ~ N-1번까지
graph = [[] for _ in range(0, N)]
for i in range(0, M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

answer = dijkstra()
print(answer)