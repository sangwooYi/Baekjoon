import sys
import heapq
sys.stdin = open("baek18352.txt")



def dijkstra():

    INF = 987654321
    dist = [INF] * (N+1)

    dist[X] = 0
    hq = []
    heapq.heappush(hq, (0, X))

    while hq:
        cost, node = heapq.heappop(hq)

        if dist[node] < cost:
            continue
        for next_node, next_cost in graph[node]:
            if dist[next_node] <= cost+next_cost:
                continue
            dist[next_node] = cost+next_cost
            heapq.heappush(hq, (dist[next_node], next_node))
    return dist



# 이문제는 가중치가 별도로 없다.
N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(0, N+1)]
for i in range(0, M):
    a, b = map(int, sys.stdin.readline().split())

    # 가중치는 1, 단방향 도로다 주의!
    graph[a].append((b, 1))

res_list = dijkstra()

flag = False
for i in range(1, N+1):
    if res_list[i] == K:
        print(i)
        flag = True

if not flag:
    print(-1)