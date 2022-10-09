import sys
import heapq
sys.stdin = open("baek14950.txt")


"""
MST

출발지점이 안정해졌을 경우는 크루스칼
(유니온-파인드 (분리집합))

출발지점이 정해졌으면 프림
(heapq, 우선순위큐)
"""

def prim_MST(graph, n, t):

    visited = [False] * (n+1)
    visited[1] = True
    hq = []
    for next_node, next_cost in graph[1]:
        # 몇번째 정복인지도 기록해야함
        heapq.heappush(hq, (next_cost, next_node))

    total_cost = 0
    cnt = 0
    while hq:
        cost, node = heapq.heappop(hq)
        # 방문처리를 여기서 체크해줘야 확실하게 MST 구현이 가능함
        if visited[node]:
            continue
        visited[node] = True
        total_cost += (cost + t*cnt)
        cnt += 1
        for next_node, next_cost in graph[node]:
            if visited[next_node]:
                continue
            heapq.heappush(hq, (next_cost, next_node))
    return total_cost


N, M, T = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(0, N+1)]
for i in range(0, M):
    a, b, c = map(int, sys.stdin.readline().split())
    # 양방향 도로이다.
    graph[a].append((b, c))
    graph[b].append((a, c))
    
answer = prim_MST(graph, N, T)
print(answer)