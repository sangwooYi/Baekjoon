import sys
import heapq
sys.stdin = open("baek1197.txt")

"""
MST 최소 신장트리 알고리즘!

visited 함수 선언후 1번노드 부터 시작
1번노드에서 갈 수 있는 모든 노드 체크,
=> 그다음부터 heapq 이용,
현재 갈 수 있는 곳 중 최솟값을 체크,
방문처리후, 그다음 갈 수 있는 모든 곳 체크
이걸 모든 노드 거칠 떄 까지 반복!
=> 이것의 결과가 Minimum Spanning Tree!!@
이 알고리즘도 익혀두자!

"""

V, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(0, V+1)]

for i in range(0, E):
    a, b, c = map(int, sys.stdin.readline().split()) 
    graph[a].append((c, b))
    graph[b].append((c, a))

visited = [False] * (V+1)
visited[1] = True
hq = []
for cost, node in graph[1]:
    heapq.heappush(hq, (cost, node))
total_cost = 0
while hq:
    now_cost, now_node = heapq.heappop(hq)
    if visited[now_node]:
        continue
    visited[now_node] = True
    total_cost += now_cost
    for next_cost, next_node in graph[now_node]:
        if visited[next_node]:
            continue
        heapq.heappush(hq, (next_cost, next_node))
print(total_cost)