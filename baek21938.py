import sys
from collections import deque
sys.stdin = open("baek21938.txt")


def bfs(start_row, start_col):

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
            if MAP[next_row][next_col] and not visited[next_row][next_col]:
                visited[next_row][next_col] = True
                que.append((next_row, next_col))


N, M = map(int, sys.stdin.readline().split())

MAP = [[0] * M for _ in range(0, N)]
for i in range(0, N):

    cur = list(map(int, sys.stdin.readline().split()))

    for j in range(0, M):
        tmp_sum = 0        
        for k in range(0, 3):
            tmp_sum += cur[3*j+k]
        MAP[i][j] = tmp_sum//3

T = int(sys.stdin.readline().rstrip())

for r in range(0, N):
    for c in range(0, M):
        if MAP[r][c] >= T:
            MAP[r][c] = 255
        else:
            MAP[r][c] = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [[False] * M for _ in range(0, N)]

cnt = 0

for r in range(0, N):
    for c in range(0, M):
        if MAP[r][c] and not visited[r][c]:
            cnt += 1
            bfs(r, c)
print(cnt)