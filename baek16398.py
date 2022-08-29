import sys
sys.stdin = open("baek16398.txt")


"""
최소신장트리
크루스칼 vs MST
출발 지점이 정해졌다면? MST
=> 아니라면 모든 출발점에 대해 다 따져보아야 하므로
(우선순위큐, visited 안했다면 방문처리 후 현재 노드에서 갈수있는 모든 노드 체크, 아니면 pass)
아니라면? 크루스칼
=> 결국 모든 간선들에 대해 find-union을 하여야 하므로, 자칫 더 비효율적일 수있다
"""

def find(x):
    if parent[x] == x:
        return x
    px = find(parent[x])
    parent[x] = px
    return px 

def union(x, y):
    px = find(x)
    py = find(y)
    if px < py:
        parent[py] = px
    else:
        parent[px] = py

N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))

graphs = []
parent = [i for i in range(0, N)]

for i in range(0, N-1):
    for j in range(i+1, N):
        graphs.append([i, j, MAP[i][j]])

graphs.sort(key=lambda x : x[2])

answer = 0
for graph in graphs:
    s, e, c = graph
    if find(s) != find(e):
        union(s, e)
        answer += c
print(answer)