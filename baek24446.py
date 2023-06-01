import sys
sys.stdin = open("baek24446.txt")
from collections import deque


N, M, R = map(int, input().split())
graph = [[] for _ in range(0, N+1)]

node_depth = [-1] * (N+1)
for i in range(0, M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

node_depth[R] = 0
que = deque()
que.append((R, 0))

while que:
    node, depth = que.popleft()

    for next_node in graph[node]:
        if node_depth[next_node] == -1:
            node_depth[next_node] = depth+1
            que.append((next_node, depth+1))
for i in range(1, N+1):
    print(node_depth[i])