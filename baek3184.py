import sys
sys.stdin = open("baek3184.txt")
from collections import deque

"""
가장자리까는 탈출이 가능한곳으로 인지한다.

따라서 가장자리부터 먼저 탐색 
=> 얘네들은 방문체크만

그다음부터는 안쪽에서 체크 
(가장자리부터 이미 체크했으므로, 무조건 영역이 존재하는 애들임)
따라서 이때부터는 양, 늑대 숫자 체크해도 된다.
양, 늑대 숫자를 반환한 후,
늑대 >= 양이면 양 - 
반대면 늑대 -
"""

def bfs(start_row, start_col):

    visited[start_row][start_col] = True
    sheep_cnt = 0
    wolf_cnt = 0

    if MAP[start_row][start_col] == WOLF:
        wolf_cnt += 1
    if MAP[start_row][start_col] == SHEEP:
        sheep_cnt += 1

    que = deque()
    que.append((start_row, start_col))

    while que:
        row, col = que.popleft()

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= R or next_col >= C:
                continue
            if visited[next_row][next_col]:
                continue
            if MAP[next_row][next_col] == BORDER:
                continue
            visited[next_row][next_col] = True
            if MAP[next_row][next_col] == SHEEP:
                sheep_cnt += 1
            if MAP[next_row][next_col] == WOLF:
                wolf_cnt += 1
            que.append((next_row, next_col))

    return (sheep_cnt, wolf_cnt)

BLANK = "."
SHEEP = "o"
WOLF = "v"
BORDER = "#"

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
R, C = map(int, input().split())
MAP = [0] * R
for i in range(0, R):
    MAP[i] = list(input())

visited = [[False] * C for _ in range(0, R)]

total_wolf = 0
total_sheep = 0

for i in range(0, R):
    for j in range(0, C):
        if MAP[i][j] == SHEEP:
            total_sheep += 1
        if MAP[i][j] == WOLF:
            total_wolf += 1


# 우선 가장자리부터 체크
for i in range(0, C):
    if MAP[0][i] != BORDER and not visited[0][i]:
        bfs(0, i)
for i in range(0, C):
    if MAP[R-1][i] != BORDER and not visited[R-1][i]:
        bfs(R-1, i)
for i in range(0, R):
    if MAP[i][0] != BORDER and not visited[i][0]:
        bfs(i, 0)
for i in range(0, R):
    if MAP[i][C-1] != BORDER and not visited[i][C-1]:
        bfs(i, C-1)

for i in range(1, R-1):
    for j in range(1, C-1):
        if MAP[i][j] != BORDER and not visited[i][j]:
            sheep, wolf = bfs(i, j)

            if sheep > wolf:
                total_wolf -= wolf
            else:
                total_sheep -= sheep

print(f"{total_sheep} {total_wolf}")