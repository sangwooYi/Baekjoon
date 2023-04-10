import sys
from collections import deque
sys.stdin = open("baek14940.txt")


N, M = map(int, sys.stdin.readline().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, sys.stdin.readline().split()))

visited = [[-1] * M for _ in range(0, N)]

que = deque()
for r in range(0, N):
    for c in range(0, M):
        if MAP[r][c] == 2:
            visited[r][c] = 0
            que.append((r, c, 0))
        if MAP[r][c] == 0:
            visited[r][c] = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while que:
    row, col, path = que.popleft()

    for d in range(0, 4):
        next_row = row + dr[d]
        next_col = col + dc[d]

        if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
            continue
        # 0이면 못감 & 아직 방문 안한곳만 체크
        if MAP[next_row][next_col] and visited[next_row][next_col] == -1:
            visited[next_row][next_col] = path+1
            que.append((next_row, next_col, path+1))

for i in range(0, N):
    print(" ".join(map(str, visited[i])))