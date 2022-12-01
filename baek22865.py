import sys
import heapq
sys.stdin = open("baek22865.txt")


def dijkstra(start):

    dist = [INF] * (N+1)
    hq = []
    dist[start] = 0
    heapq.heappush(hq, (0, start))
    
    while hq:
        cost, node = heapq.heappop(hq)

        for next_node, next_cost in graph[node]:
            if dist[next_node] <= cost+next_cost:
                continue
            dist[next_node] = cost+next_cost
            heapq.heappush(hq, (dist[next_node], next_node))
    return dist


INF = 9876543212
N = int(sys.stdin.readline())
A, B, C = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
graph = [[] for _ in range(0, N+1)]

max_len = 0
answer_node = 0
for i in range(0, M):
    d, e, l = map(int, sys.stdin.readline().split())

    # 양방향
    graph[d].append((e, l))
    graph[e].append((d, l))

# 시간 절약용!
a_dist = dijkstra(A)
b_dist = dijkstra(B)
c_dist = dijkstra(C)

answer_node = 0
max_len = 0
for i in range(1, N+1):
    tmp_min = min(a_dist[i], b_dist[i], c_dist[i])

    if tmp_min > max_len:
        max_len = tmp_min
        answer_node = i
print(answer_node)

