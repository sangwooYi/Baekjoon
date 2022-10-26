import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("baek18116.txt")


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
        cnt[px] += cnt[py]
    else:
        parent[px] = py
        cnt[py] += cnt[px]


N = int(sys.stdin.readline())
parent = [i for i in range(0, 1000001)]
cnt = [1] * 1000001
for _ in range(0, N):
    oper = list(sys.stdin.readline().split())
    if oper[0] == "I":
        a = int(oper[1])
        b = int(oper[2])
        if find(a) != find(b):
            union(a, b)
    elif oper[0] == "Q":
        a = int(oper[1])
        pa = find(a)
        print(cnt[pa])