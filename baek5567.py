import sys
sys.stdin = open("baek5567.txt")
from collections import deque


def bfs():
    cnt = 0
    visited = [False] * (N+1)
    visited[1] = True
    que = deque()
    que.append((1, 0))

    while que:
        node, path = que.popleft()

        for next_node in graph[node]:
            if visited[next_node]:
                continue
            next_path = path+1
            if next_path > 2:
                continue
            cnt += 1
            visited[next_node] = True
            que.append((next_node, next_path))
    return cnt

N = int(input())
M = int(input())
graph = [[] for _ in range(0, N+1)]

for i in range(0, M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = bfs()
print(answer)