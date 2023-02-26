import sys
sys.stdin = open("baek4963.txt")
from collections import deque



def bfs(start_row, start_col):
    visited[start_row][start_col] = True

    que = deque()
    que.append((start_row, start_col))

    while que:
        row, col = que.popleft()

        for d in range(0, 8):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= H or next_col >= W:
                continue
            if MAP[next_row][next_col] == 0:
                continue
            if visited[next_row][next_col]:
                continue
            visited[next_row][next_col] = True
            que.append((next_row, next_col))


# 대각선까지 포함
#좌상, 상, 우상, 우, 우하, 하, 좌하, 좌
dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]
while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    MAP = [0] * H
    visited = [[False] * W for _ in range(0, H)]
    for i in range(0, H):
        MAP[i] = list(map(int, input().split()))
    
    cnt = 0
    for i in range(0, H):
        for j in range(0, W):
            if MAP[i][j] and not visited[i][j]:
                cnt += 1
                bfs(i, j)
    print(cnt)