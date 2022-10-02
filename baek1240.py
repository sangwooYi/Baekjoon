import sys
from collections import deque
sys.stdin = open("baek1240.txt")


"""

"""

def bfs(start, end):
    que = deque()
    que.append((start, 0))
    visited = [False] * (N+1)
    visited[start] = True

    while que:
        now, cost = que.popleft()

        if now == end:
            return cost
        for next_node, next_cost in graph[now]:
            if visited[next_node]:
                continue
            visited[next_node] = True
            que.append((next_node, cost+next_cost))


N, M = map(int, input().split())
graph = [[] for _ in range(0, N+1)]
for i in range(0, N-1):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
    graph[e].append((s, c))

for i in range(0, M):
    s, e = map(int, input().split())
    res = bfs(s, e)
    print(res)