import sys
sys.stdin = open("baek7511.txt")


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

T = int(sys.stdin.readline())

for tc in range(1, T+1):
    
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())

    parent = [i for i in range(0, N)]
    
    for i in range(0, K):
        a, b = map(int, sys.stdin.readline().split())

        union(a, b)
    M = int(sys.stdin.readline())
    
    print(f"Scenario {tc}:")
    for i in range(0, M):
        a, b = map(int, sys.stdin.readline().split())

        if find(a) == find(b):
            print(1)
        else:
            print(0)
    print()
