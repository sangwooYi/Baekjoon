import sys
# 기본적으로 재귀깊이가 1000밖에안됨. 따라서 dfs 쓸 때는 이거 무조건 설정하자
sys.setrecursionlimit(10**5+1000)
sys.stdin = open("baek21937.txt")


def dfs(node):
    global cnt
    for next_node in graph[node]:
        if not visited[next_node]:
            cnt += 1
            visited[next_node] = True
            dfs(next_node)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(0, N+1)]

# a -> b 면 역으로 b->a 로 저장하자
for i in range(0, M):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

X = int(sys.stdin.readline())

cnt = 0
visited = [False] * (N+1)
dfs(X)
print(cnt)