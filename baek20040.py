import sys
sys.setrecursionlimit(5*(10**4))
sys.stdin = open("baek20040.txt")


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


N, M = map(int, sys.stdin.readline().split())
parent =  [i for i in range(0, N)]

answer = 0
for i in range(0, M):
    a, b = map(int, sys.stdin.readline().split())
    if find(a) == find(b):
        answer = i+1
        break
    union(a, b)
print(answer)
