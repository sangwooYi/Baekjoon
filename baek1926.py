import sys
sys.stdin = open("baek1926.txt")
from collections import deque


def bfs(start_row, start_col):

    cnt = 1
    visited[start_row][start_col] = True
    que = deque()
    que.append((start_row, start_col))

    while que:
        row, col = que.popleft()

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
                continue
            if visited[next_row][next_col]:
                continue
            if MAP[next_row][next_col]:
                cnt += 1
                visited[next_row][next_col] = True
                que.append((next_row, next_col))
    return cnt


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N, M = map(int, input().split())
MAP = [0] * N
visited = [[False] * M for _ in range(0, N)]
area_cnt = 0
max_area = 0
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))


for i in range(0, N):
    for j in range(0, M):
        if not visited[i][j] and MAP[i][j]:
            now = bfs(i, j)
            area_cnt += 1
            max_area = max(max_area, now)
print(area_cnt)
print(max_area)