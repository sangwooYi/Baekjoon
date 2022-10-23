import sys
from collections import deque
sys.stdin = open("baek2644.txt")

def calc_term(graph, a, b, n):

    que = deque()
    visited = [False] * (n+1)
    que.append((a, 0))
    visited[a] = True

    while que:
        node, path = que.popleft()
        for next_node in graph[node]:
            if visited[next_node]:
                continue
            if next_node == b:
                return path+1
            visited[next_node] = True
            que.append((next_node, path+1))
    return -1

N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = [[] for _ in range(0, N+1)]
for i in range(0, M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

answer = calc_term(graph, A, B, N)
print(answer)