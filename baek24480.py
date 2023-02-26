import sys
sys.setrecursionlimit(10**5)
sys.stdin = open("baek24480.txt")

"""
인접정점은 내림차순으로 방문!
"""


def dfs(node):
    global cnt
    visited[node] = True
    visit_order[node] = cnt

    graph[node].sort(key=lambda x : -x)
    for next_node in graph[node]:
        if not visited[next_node]:
            cnt += 1
            dfs(next_node)







N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(0, N+1)]
for i in range(0, M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (N+1)
visit_order = [0] * (N+1)
cnt = 1
dfs(R)
for i in range(1, N+1):
    print(visit_order[i])