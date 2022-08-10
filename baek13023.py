import sys
sys.stdin = open("baek13023.txt")

def dfs(now, visited, cnt):
    global answer
    
    for next_node in graph[now]:
        if visited[next_node]:
            continue
        # 종료 조건
        if cnt+1 == 5:
            answer = 1
            return
        visited[next_node] = True
        dfs(next_node, visited, cnt+1)
        visited[next_node] = False



N, M = map(int, input().split())
graph = [[] for _ in range(0, N)]



nodes = set()
for i in range(0, M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    nodes.add(a)
    nodes.add(b)

nodes = list(nodes)

answer = 0
for node in nodes:
    check = [False] * N
    check[node] = True
    dfs(node, check, 1)

print(answer)
