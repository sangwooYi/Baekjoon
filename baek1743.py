import sys
sys.stdin = open("baek1743.txt")
from collections import deque


def check_area(start_row, start_col):

    visited[start_row][start_col] = True
    que = deque()
    que.append((start_row, start_col))

    area = 1
    while que:
        row, col = que.popleft()

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
                continue
            if MAP[next_row][next_col] and not visited[next_row][next_col]:
                area += 1
                visited[next_row][next_col] = True
                que.append((next_row, next_col))
    return area

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N, M, K = map(int, input().split())
MAP = [[0] * M for _ in range(0, N)]
visited = [[False]  * M for _ in range(0, N)]


max_area = 0
for i in range(0, K):
    r, c = map(int, input().split())
    MAP[r-1][c-1] = 1

for i in range(0, N):
    for j in range(0, M):
        if MAP[i][j] and not visited[i][j]:
            now_area = check_area(i, j)
            max_area = max(max_area, now_area)
print(max_area)

