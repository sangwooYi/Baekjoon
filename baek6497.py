import sys
sys.stdin = open("baek6497.txt")


"""
MST
시작점이 정해져있으면 프림! 
(heapq)

아니라면 크루스칼
(find-union)
"""

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

while True:
    M, N = map(int, sys.stdin.readline().split())
    if M == 0 and N == 0:
        break
    nodes = [0] * N
    parent = [i for i in range(0, M)]
    total_sum = 0
    for i in range(0, N):
        a, b, c = map(int, sys.stdin.readline().split())
        nodes[i] = (c, a, b)
        total_sum += c
    # 그냥 sort 떄리면 알아서 1번요소 > 2번요소 > 3번요소 순으로 내림차순 해줌!
    nodes.sort()

    min_req = 0
    for node in nodes:
        cost, a, b = node

        if find(a) != find(b):
            union(a, b)
            min_req += cost
    print(total_sum-min_req)