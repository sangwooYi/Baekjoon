import sys
sys.stdin = open("baek14496.txt")
from collections import deque


def bfs():

    visited = [False] * (N+1)
    que = deque()
    visited[A] = True
    que.append((A, 0))

    while que:
        now, cnt = que.popleft()

        if now == B:
            return cnt

        for next_node in graph[now]:
            if visited[next_node]:
                continue
            visited[next_node] = True
            que.append((next_node, cnt+1))
    return -1



A, B = map(int, input().split())
N, M = map(int, input().split())

graph = [[] for _ in range(0, N+1)]

for i in range(0, M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

ans = bfs()
print(ans)