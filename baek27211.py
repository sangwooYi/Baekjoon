import sys
from collections import deque
sys.stdin = open("baek27211.txt")


def bfs(start_row, start_col):
    
    que = deque()
    que.append((start_row, start_col))

    while que:
        row, col = que.popleft()

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            # 경계를 벗어나도 반대편과 연결 됨
            if next_row < 0:
                next_row = N-1
            if next_row >= N:
                next_row = 0
            if next_col < 0:
                next_col = M-1
            if next_col >= M:
                next_col = 0
            if MAP[next_row][next_col]:
                continue
            if visited[next_row][next_col]:
                continue
            visited[next_row][next_col] = True
            que.append((next_row, next_col))
N, M = map(int, sys.stdin.readline().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, sys.stdin.readline().split()))


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [[False] * M for _ in range(0, N)]
cnt = 0

for i in range(0, N):
    for j in range(0, M):
        if MAP[i][j]:
            continue
        if visited[i][j]:
            continue
        cnt += 1
        visited[i][j] = True
        bfs(i, j)
print(cnt)