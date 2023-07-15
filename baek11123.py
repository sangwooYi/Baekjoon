import sys
sys.stdin = open("baek11123.txt")
from collections import deque

def check_area(start_row, start_col):

    que = deque()
    que.append((start_row, start_col))

    while que:
        row, col = que.popleft()

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= H or next_col >= W:
                continue
            if visited[next_row][next_col]:
                continue
            if MAP[next_row][next_col] == ".":
                continue
            visited[next_row][next_col] = True
            que.append((next_row, next_col))


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = int(input())
for tc in range(0, T):
    H, W = map(int, input().split())
    MAP = [0] * H
    for i in range(0, H):
        MAP[i] = list(input())
    
    visited = [[False] * W for _ in range(0, H)]
    cnt = 0

    for r in range(0, H):
        for c in range(0, W):
            if MAP[r][c] == "#" and not visited[r][c]:
                cnt += 1
                check_area(r, c)
    print(cnt)