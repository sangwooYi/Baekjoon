from collections import deque


# 좌상 상 우상 우 우하 하 좌하 좌 
dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]


def bfs(start_row, start_col):
    visited[start_row][start_col] = True
    que = deque()
    que.append((start_row, start_col))

    while que:
        row, col = que.popleft()

        for d in range(0, 8):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= M or next_col >= N:
                continue
            if MAP[next_row][next_col] and not visited[next_row][next_col]:
                visited[next_row][next_col] = True
                que.append((next_row, next_col))

M, N = map(int, input().split())
MAP = [0] * M
visited = [[False] * N for _ in range(0, M)]
for i in range(0, M):
    MAP[i] = list(map(int, input().split()))

cnt = 0
for i in range(0, M):
    for j in range(0, N):
        if MAP[i][j] and not visited[i][j]:
            cnt += 1
            bfs(i, j)
print(cnt)