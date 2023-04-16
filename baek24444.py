import sys
sys.stdin = open("baek24444.txt")

from collections import deque


N, M, R = map(int, input().split())

graph = [[] for _ in range(0, N+1)]

for i in range(0, M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)
que = deque()
visited[R] = 1

for i in range(1, N+1):
    graph[i].sort()

que.append((R, 1))

cnt = 0
while que:
    node, path = que.popleft()
    for next_node in graph[node]:
        if visited[next_node]:
            continue
        cnt += 1
        visited[next_node] = 1+cnt
        que.append((next_node, 1+cnt))

for i in range(1, N+1):
    print(visited[i])
