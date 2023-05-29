import sys
sys.setrecursionlimit(10**5)
sys.stdin = open("baek24482.txt")


def dfs(node, depth):

    for next_node in graph[node]:
        # 아직 방문 안한경우만
        if visited[next_node] == -1:
            visited[next_node] = depth+1
            dfs(next_node, depth+1)


N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(0, N+1)]
visited = [-1] * (N+1)
for _ in range(0, M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    if len(graph[i]) > 0:
        graph[i].sort(key=lambda x : -x)

visited[R] = 0
dfs(R, 0)

for i in range(1, N+1):
    print(visited[i])