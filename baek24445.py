import sys
from collections import deque
sys.stdin = open("baek24445.txt")



N, M, R = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(0, N+1)]

for i in range(0, M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort(reverse=True)

visited = [0] * (N+1)

que = deque()
visited[R] = 1
que.append(R)

cnt = 1
while que:
    node = que.popleft()

    for next_node in graph[node]:
        if visited[next_node]:
            continue
        cnt += 1
        visited[next_node] = cnt
        que.append(next_node)

for i in range(1, N+1):
    print(visited[i])