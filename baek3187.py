import sys
sys.stdin = open("baek3187.txt")
from collections import deque


def check_bfs(start_row, start_col):

    que = deque()
    que.append((start_row, start_col))

    cur_wolves_cnt = 0
    cur_sheep_cnt = 0
    while que:
        row, col = que.popleft()

        if MAP[row][col] == WOLF:
            cur_wolves_cnt += 1
        if MAP[row][col] == SHEEP:
            cur_sheep_cnt += 1

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= R or next_col >= C:
                continue
            if MAP[next_row][next_col] == FENCE:
                continue
            if visited[next_row][next_col]:
                continue
            visited[next_row][next_col] = True
            que.append((next_row, next_col))
    if cur_sheep_cnt == 0 and cur_wolves_cnt == 0:
        return -1
    if cur_sheep_cnt > cur_wolves_cnt:
        return (WOLF, cur_wolves_cnt)
    return (SHEEP, cur_sheep_cnt)


FENCE = "#"
SHEEP = "k"
WOLF = "v"

dr = [-1, 1, 0, 0]
dc = [0 ,0, -1, 1]
R, C = map(int, input().split())
MAP = [0] * R
for i in range(0, R):
    MAP[i] = list(input())

visited = [[False] * C for _ in range(0, R)]

total_wolves_cnt = 0
total_sheep_cnt = 0
for r in range(0, R):
    for c in range(0, C):
        if MAP[r][c] == WOLF:
            total_wolves_cnt += 1
        if MAP[r][c] == SHEEP:
            total_sheep_cnt += 1

for r in range(0, R):
    for c in range(0, C):
        if MAP[r][c] != FENCE and not visited[r][c]:
            visited[r][c] = True
            res = check_bfs(r, c)
            if res == -1:
                continue
            if res[0] == WOLF:
                total_wolves_cnt -= res[1]
            if res[0] == SHEEP:
                total_sheep_cnt -= res[1]
print(f"{total_sheep_cnt} {total_wolves_cnt}")