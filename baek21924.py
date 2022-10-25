import sys
sys.stdin = open("baek21924.txt")


def find(x):
    if x == parent[x]:
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


total = 0
N, M = map(int, sys.stdin.readline().split())
edges = [0] * M
parent = [i for i in range(0, N+1)]
for i in range(0, M):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[i] = (c, a, b)
    total += c

edges.sort()

min_cost = 0
for edge in edges:
    cost, a, b = edge

    if find(a) != find(b):
        union(a, b)
        min_cost += cost
answer = -1
flag = True


root_node = find(1)
for i in range(2, N+1):
    if root_node != find(i):
        flag = False
        break
if flag:
    answer = total-min_cost
print(answer)
