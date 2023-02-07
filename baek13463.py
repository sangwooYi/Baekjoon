import sys
from collections import deque
sys.stdin = open("baek13463.txt")

def mod_if_left(node):
    cnt = 0
    for next_node in graph[node]:
        if visited[next_node] == LEFT:
            cnt += 1
    total_partner = len(graph[node])
    limit_left = total_partner/2
    if cnt >= limit_left:
        visited[node] = LEFT
    else:
        visited[node] = STAY


def bfs():
    if X == L:
        return LEFT
    visited[L] = LEFT
    que = deque()
    que.append(L)

    while que:
        node = que.popleft()

        for next_node in graph[node]:
            if visited[next_node]:
                continue
            mod_if_left(next_node)
            que.append(next_node)
            if visited[next_node] == LEFT:
                for n_n_node in graph[next_node]:
                    if visited[n_n_node] == STAY:
                        mod_if_left(n_n_node)
    return visited[next_node]



C, P, X, L = map(int, sys.stdin.readline().split())
LEFT = 1
STAY = -1
graph = [[] for _ in range(0, C+1)]
for i in range(0, P):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (C+1)
answer = bfs()
if answer == LEFT:
    print("leave")
else:
    print("stay")
