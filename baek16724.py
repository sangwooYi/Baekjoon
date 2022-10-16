import sys
sys.stdin = open("baek16724.txt")


def find(x):
    if x == parent[x[0]][x[1]]:
        return x
    px = find(parent[x[0]][x[1]])
    parent[x[0]][x[1]] = px
    return px


def union(x, y):
    px = find(x)
    py = find(y)

    if px[0] <= py[0] and px[1] <= py[1]:
        parent[py[0]][py[1]] = px
    else:
        parent[px[0]][px[1]] = py

N, M = map(int, sys.stdin.readline().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(sys.stdin.readline().rstrip())

parent = [[[i, j] for j in range(0, M)] for i in range(0, N)]

directs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
dir_dict = { "U": 0, "D": 1, "L": 2, "R": 3 }
for row in range(0, N):
    for col in range(0, M):
        now_dir = MAP[row][col]
        direct = dir_dict[now_dir]
        next_row = row + directs[direct][0]
        next_col = col + directs[direct][1]
        # 지도 나가는 방향 없음!
        union([row, col], [next_row, next_col])

cnt = 0
tmp_dict = {}
for row in range(0, N):
    for col in range(0, M):
        tmp = find([row, col])
        safe_zone = (tmp[0], tmp[1])
        if safe_zone not in tmp_dict.keys():
            cnt += 1
            tmp_dict[safe_zone] = 1
print(cnt)
