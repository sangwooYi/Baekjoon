import sys
sys.stdin = open("baek17352.txt")


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

N = int(sys.stdin.readline())
parent = [i for i in range(0, N+1)]

for i in range(0, N-2):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b)

head_node = find(1)

for i in range(2, N+1):
    if find(i) != head_node:
        target_node = i
        break
print(head_node, target_node)