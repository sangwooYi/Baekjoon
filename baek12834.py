import sys
import heapq
sys.stdin = open("baek12834.txt")


def dijkstra(graph, start, end):

    dist = [INF] * (V+1)
    dist[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))

    while hq:
        cost, node = heapq.heappop(hq)

        if dist[node] < cost:
            continue
        for next_node, next_cost in graph[node]:
            # 현재 지점까지 도달만 하면 그다음은 결국 동일하므로 == 인 경우도 제껴도 됨! (레이저 통신처럼 아닌 문제도 있으니 조심!)
            if dist[next_node] <= cost + next_cost:
                continue
            dist[next_node] = cost + next_cost
            heapq.heappush(hq, (dist[next_node], next_node))
    if dist[end] == INF:
        return -1
    return dist[end]

N, V, E = map(int, input().split())
A, B = map(int, input().split())
H = list(map(int, input().split()))
INF = 987654321
graph = [[] for _ in range(0, V+1)]

for i in range(0, E):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

answer = 0
for i in range(0, N):
    a_res = dijkstra(graph, H[i], A)
    b_res = dijkstra(graph, H[i], B)

    if a_res == -1 and b_res == -1:
        answer += -1
    else:
        answer += (a_res + b_res)
print(answer)