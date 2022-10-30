import sys
from collections import deque
sys.stdin = open("baek15591.txt")


def calc_usado(graph, k, v):
    cnt = 0
    visited = [False] * (N+1)
    que = deque()
    visited[v] = True
    
    for node, usado in graph[v]:
        visited[node] = True
        if usado >= k:
            cnt += 1
        que.append((node, usado))

    while que:
        node, usado = que.popleft()

        for next_node, n_usado in graph[node]:
            if visited[next_node]:
                continue
            visited[next_node] = True
            next_usado = min(usado, n_usado)
            if next_usado >= k:
                cnt += 1
            que.append((next_node, next_usado))
    return cnt

N, Q = map(int, input().split())
graph = [[] for _ in range(0, N+1)]
for i in range(0, N-1):
    a, b, r = map(int, input().split())
    graph[a].append((b, r))
    graph[b].append((a, r))

quests = [0] * Q
for i in range(0, Q):
    k, v = map(int, input().split())
    ans = calc_usado(graph, k, v)
    print(ans)