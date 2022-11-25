import sys
import math
sys.stdin = open("baek10216.txt")


def calc_distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)


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


T = int(input())
for tc in range(0, T):
    N = int(input())
    parent = [i for i in range(0, N)]
    positions = [0] * N
    for i in range(0, N):
        positions[i] = list(map(int, input().split()))

    visited = [False] * N

    for i in range(0, N):
        for j in range(i+1, N):
            x1, y1, range1 = positions[i]
            x2, y2, range2 = positions[j]

            if calc_distance(x1, y1, x2, y2) <= range1+range2:
                if find(i) != find(j):
                    union(i, j)

    cnt_dict = {}
    answer = 0
    for i in range(0, N):
        head_node = find(i)
        if head_node not in cnt_dict.keys():
            answer += 1
            cnt_dict[head_node] = 1
    print(answer)