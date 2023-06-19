import sys
sys.stdin = open("baek17086.txt")
from collections import deque


def bfs(start_row, start_col):

    que = deque()
    que.append((start_row, start_col, 0))
    visited = [[False] * M for _ in range(0, N)]

    while que:
        row, col, path = que.popleft()

        for d in range(0, 8):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
                continue
            if visited[next_row][next_col]:
                continue
            if MAP[next_row][next_col] == 1:
                return path+1
            visited[next_row][next_col] = True
            que.append((next_row, next_col, path+1))

# 8 방향 가능
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

N, M = map(int, input().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))

max_ans = 0
for r in range(0, N):
    for c in range(0, M):
        if MAP[r][c] == 0:
            safe_len = bfs(r, c)
            max_ans = max(max_ans, safe_len)
print(max_ans)
