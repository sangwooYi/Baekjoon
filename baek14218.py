import sys
from collections import deque
sys.stdin = open("baek14218.txt")


def bfs():

    visited = [-1] * (N+1)
    que = deque()
    visited[1] = 0
    que.append((1, 0))

    while que:
        node, path = que.popleft()

        for next_node in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = path+1
                que.append((next_node, path+1))
    return visited

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(0, N+1)]

for _ in range(0, M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

Q = int(sys.stdin.readline().rstrip())
for _ in range(0, Q):
    a, b = map(int, sys.stdin.readline().split())
    
    graph[a].append(b)
    graph[b].append(a)

    cur = bfs()
    print(" ".join(map(str, cur[1:])))