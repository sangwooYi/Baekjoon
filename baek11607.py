import sys
from collections import deque
sys.stdin = open("baek11607.txt")


def bfs():
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited = [[-1] * M for _ in range(0, N)]
    visited[0][0] = 0
    que = deque()
    que.append((0, 0, 0))

    while que:
        row, col, path = que.popleft()
        jump = MAP[row][col]

        for d in range(0, 4):
            next_row = row + dr[d]*jump
            next_col = col + dc[d]*jump

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
                continue
            if visited[next_row][next_col] != -1:
                continue
            if next_row == N-1 and next_col == M-1:
                return path+1
            if MAP[next_row][next_col]:
                visited[next_row][next_col] = path+1
                que.append((next_row, next_col, path+1))

    return "IMPOSSIBLE"

N, M = map(int, input().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input()))

answer = bfs()
print(answer)