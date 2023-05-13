import sys
sys.setrecursionlimit(10**5)
sys.stdin = open("baek24479.txt")

def dfs(node):
    global order
    visited[node] = order
    order += 1
    graph[node].sort()
    for next_node in graph[node]:
        if visited[next_node]:
            continue
        dfs(next_node)    

N, M, R = map(int, sys.stdin.readline().split())
visited = [0] * (N+1)
graph = [[] for _ in range(0, N+1)] 
for i in range(0, M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
order = 1
dfs(R)

for i in range(1, N+1):
    print(visited[i])