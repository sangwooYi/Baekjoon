import sys
sys.stdin = open("baek11085.txt")

"""
크루스칼 알고리즘을
역으로 최댓값부터 순회한다고 생각하면 좋음!

아이디어가 중요!
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

    if px <= py:
        parent[py] = px
    else:
        parent[px] = py


P, W = map(int, input().split())
C, V = map(int, input().split())

parent = [i for i in range(0, P)]
edges = [0] * W
for i in range(0, W):
    edges[i] = list(map(int, input().split()))

edges.sort(key=lambda x : -x[2])


for edge in edges:
    a, b, w = edge
    union(a, b)

    if find(C) == find(V):
        answer = w
        break
print(answer)