import sys
sys.stdin = open("baek10157.txt")

"""
row 는 반대
col 은 같은방향
"""

C, R = map(int, input().split())
K = int(input())

MAP = [[0] * C for _ in range(0, R)]

# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

chk_map = {}
total = R*C
cnt = 0
d = 0

row = R-1
col = 0
while cnt < total:
    cnt += 1
    MAP[row][col] = cnt
    chk_map[cnt] = [R-row, col+1]

    next_row = row + dr[d]
    next_col = col + dc[d]

    flag = False    
    if next_row < 0 or next_col < 0 or next_row >= R or next_col >= C:
        flag = True
    elif MAP[next_row][next_col]:
        flag = True

    if flag:
        d = (d+1)%4
    row = row + dr[d]
    col = col + dc[d]

if K > total:
    print(0)
else:
    print(f"{chk_map[K][1]} {chk_map[K][0]}")