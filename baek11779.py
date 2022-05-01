import sys
import heapq
sys.stdin = open("baek11779.txt")
"""
다익스트라는 문제를 특히나 잘 읽자!
동일 노드에 대해, 중복된 간선이 주어지는 경우에는,
최솟값으로 업데이트를 해주어야 함!

아니 왜 메모리 초과나는건데 ... 도저히 모르겠다
"""


def dijkstra(start):
    dist[start] = 0 
    hq = []
    # cost, 현재 노드
    heapq.heappush(hq, (0, start))
    while hq:
        cost, node = heapq.heappop(hq)
        # 할필요 없음
        if dist[node] < cost:
            continue
        for next_cost, next_node in graph[node]:
            # 현재 저장된 값 이상의 값인경우 pass, == 이라도 할 이유가 없다.. 이 조건 주의!
            # 다익스트라 dist 배열 업데이트 조건은, 더 작은값이 올 때만!!!
            if dist[next_node] <= cost + next_cost:
                continue
            dist[next_node] = cost + next_cost    
            # 갱신될때마다 parent 업데이트
            parent[next_node] = node
            heapq.heappush(hq, (dist[next_node], next_node))
                       

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(0, N+1)]
for i in range(0, M):
    a, b, c = map(int, sys.stdin.readline().split())
    # 어차피, 최솟값을 쓸거임
    graph[a].append((c, b))
s, e = map(int, sys.stdin.readline().split())
INF = sys.maxsize
parent = [i for i in range(0, N+1)]
dist = [INF] * (N+1)
dijkstra(s)
print(dist[e])
path = [e]
now = e
while now != s:
    now = parent[now]
    path.append(now)
print(len(path))
path.reverse()
print(" ".join(map(str, path)))