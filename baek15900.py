import sys
sys.setrecursionlimit((10**5)*5)
sys.stdin = open("baek15900.txt")


def dfs(node, visited, turn):
    global total_turn

    flag = False
    for next_node in graph[node]:
        if not visited[next_node]:
            flag = True
            visited[next_node] = True
            dfs(next_node, visited, turn+1)
            visited[next_node] = False
    if not flag:
        total_turn += turn

N = int(sys.stdin.readline())
graph = [[] for _ in range(0, N+1)]

for i in range(0, N-1):
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)
    

total_turn = 0

visited = [False] * (N+1)
visited[1] = True
dfs(1, visited, 0)

if total_turn % 2:
    print("Yes")
else:
    print("No")