import sys
sys.stdin = open("baek2162.txt")

"""
분리 집합 그냥 
Union - Find 임!! 괜히 쫄지 말자
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
    if px < py:
        parent[py] = px
    else:
        parent[px] = py


def ccw(x1, y1, x2, y2, x3, y3):

    temp = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)
    if temp > 0:
        return 1
    elif temp < 0:
        return -1
    else:
        return 0

def is_cross(x1, y1, x2, y2, x3, y3, x4, y4):

    flag = False
    if ccw(x1, y1, x2, y2, x3, y3)*ccw(x1, y1, x2, y2, x4, y4) == 0 and ccw(x3, y3, x4, y4, x1, y1)*ccw(x3, y3, x4, y4, x2, y2) == 0:
        if min(x1, x2) <= max(x3, x4) and min(y1, y2) <= max(y3, y4) and min(x3, x4) <= max(x1, x2) and min(y3, y4) <= max(y1, y2):
            flag = True
    elif ccw(x1, y1, x2, y2, x3, y3)*ccw(x1, y1, x2, y2, x4, y4) <= 0 and ccw(x3, y3, x4, y4, x1, y1)*ccw(x3, y3, x4, y4, x2, y2) <= 0:
        flag = True
    return flag

N = int(input())
lines = [0] * N
for i in range(0, N):
    x1, y1, x2, y2 = map(int, input().split())
    lines[i] = (x1, y1, x2, y2)

parent = [i for i in range(0, N)]

for i in range(0, N):

    x1, y1, x2, y2 = lines[i]
    for j in range(0, N):
        if i == j:
            continue
        # 아직 집합관계가 아닌 경우만
        if find(i) != find(j):
            x3, y3, x4, y4 = lines[j]
            if is_cross(x1, y1, x2, y2, x3, y3, x4, y4):
                union(i, j)

count = {}
for i in range(0, N):
    pi = find(i)
    if pi in count.keys():
        count[pi] += 1
    else:
        count[pi] = 1

group_num = len(count.keys())
max_num = 0
for key in count:
    max_num = max(count[key], max_num)
print(group_num)
print(max_num)