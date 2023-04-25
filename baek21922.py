import sys
from collections import deque
sys.stdin = open("baek21922.txt")


"""
1번은 좌/우 방향 바람은 반대로 상/하는 그대로
2번은 상/하 방향은 반대로, 좌/우는 그대로
3번은 상<>우 // 하<>좌 로 바꾼다
4번은 하<>우 // 상<>좌 로 바꾼다

방향은 0상 1우 2하 3좌 로 간다.
visited 배열은 [r][c][d] 로 구성 (최대 8백만)

파이썬으로는 풀기 힘든문제 왠만하면 pass하자...
"""

def check_area():

    # 상우하좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    up = 0
    right = 1
    down = 2
    left = 3

    que = deque()
    visited = [[[False] * 4 for _ in range(0, M)] for _ in range(0, N)]
    for r in range(0, N):
        for c in range(0, M):
            if MAP[r][c] == 9:
                for d in range(0, 4):
                    visited[r][c][d] = True
                    que.append((r, c, d))

    while que:

        row, col, dir = que.popleft()

        next_row = row + dr[dir]
        next_col = col + dc[dir]

        if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
            continue
        if visited[next_row][next_col][dir]:
            continue
        visited[next_row][next_col][dir] = True
        next_dir = dir
        # 좌우가 막힌다.
        if MAP[next_row][next_col] == 1:
            # 1<->3
            if dir == left or dir == right:
                next_dir = (dir+2)%4
        # 상하가 막힌다.
        if MAP[next_row][next_col] == 2:
            # 0<->2
            if dir == up or dir == down:
                next_dir = (dir+2)%4

        # 상 <-> 우 // 하 <-> 좌 로 바뀜
        if MAP[next_row][next_col] == 3:
            if dir == 0:
                next_dir = 1
            if dir == 1:
                next_dir = 0
            if dir == 3:
                next_dir = 2
            if dir == 2:
                next_dir = 3
        # 상 <-> 좌 // 하 <-> 우 로 바뀜
        if MAP[next_row][next_col] == 4:
            if dir == 0:
                next_dir = 3
            if dir == 3:
                next_dir = 0
            if dir == 2:
                next_dir = 1
            if dir == 1:
                next_dir = 2      
        que.append((next_row, next_col, next_dir))

    cool_area = 0
    for r in range(0, N):
        for c in range(0, M):
            flag = False
            for d in range(0, 4):
                if visited[r][c][d]:
                    flag = True
                    break
            if flag:
                cool_area += 1
    return cool_area

N, M = map(int, sys.stdin.readline().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, sys.stdin.readline().split()))


answer = check_area()
print(answer)