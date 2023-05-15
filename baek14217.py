import sys
sys.stdin = open("baek14217.txt")
from collections import deque

def bfs():

    visited = [-1] * (N+1)
    visited[1] = 0
    que = deque()
    que.append(1)

    while que:
        node = que.popleft()

        for next_node in range(1, N+1):
            if node == next_node:
                continue
            if graph[node][next_node] == 1 and visited[next_node] == -1:
                visited[next_node] = visited[node]+1
                que.append(next_node)
    print(" ".join(map(str, visited[1:])))

# graph[a][b]가 1이면 길O, 0이면 길X
N, M = map(int, input().split())
graph = [[0] * (N+1) for _ in range(0, N+1)]

for i in range(0, M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

Q = int(input())
for i in range(0, Q):
    oper, a, b = map(int, input().split())
    # 이미 있는데 1이거나 없는데 2가 들어오는 경우는 X
    if oper == 1:
        graph[a][b] = 1
        graph[b][a] = 1
    else:
        graph[a][b] = 0
        graph[b][a] = 0
    bfs()