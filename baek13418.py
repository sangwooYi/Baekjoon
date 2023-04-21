import sys
sys.stdin = open("baek13418.txt")
import heapq

"""
프림 알고리즘은
MST 중, 출발지점이 정해질 때 쓰기 좋다!
(출발지점 안정해져있으면 크루스칼 (find-union) 쓰는게 훨씬 좋음)

heapq 이용하며
현재 노드에서 이동 가능한 다음 간선중 항상 최소  or 최대를 선택하여
진행하도록 스패닝 트리를 짤 수 있다!

여기서 0이 오르막길
1이 내리막길
"""


def min_heap():

    visited = [False] * (N+1)
    visited[0] = True
    
    hq = []
    for next_node, next_cost in graph[0]:
        heapq.heappush(hq, (next_cost, next_node))
    
    total_cost = 0
    while hq:
        cost, node = heapq.heappop(hq)

        if visited[node]:
            continue
        visited[node] = True
        total_cost += cost

        for next_node, next_cost in graph[node]:
            if visited[next_node]:
                continue
            heapq.heappush(hq, (next_cost, next_node))
    return total_cost**2

def max_heap():
    visited = [False] * (N+1)
    visited[0] = True
    
    hq = []
    for next_node, next_cost in graph[0]:
        heapq.heappush(hq, (-next_cost, next_node))
    
    total_cost = 0
    while hq:
        cost, node = heapq.heappop(hq)

        if visited[node]:
            continue
        visited[node] = True
        total_cost -= cost
        for next_node, next_cost in graph[node]:
            if visited[next_node]:
                continue
            heapq.heappush(hq, (-next_cost, next_node))
    return total_cost**2

N, M = map(int, input().split())
graph = [[] for _ in range(0, N+1)]
for i in range(0, M+1):
    a, b, c = map(int, input().split())
    # 1이면 0으로 0이면 1로 만든다
    if c == 0:
        c += 1
    else:
        c -= 1
    graph[a].append((b, c))
    graph[b].append((a, c))

min_cost = min_heap()
max_cost = max_heap()

print(max_cost-min_cost)