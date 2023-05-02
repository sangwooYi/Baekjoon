import sys
from collections import deque
sys.stdin = open("baek17129.txt")

def bfs():

    que = deque()

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    flag = False
    visited = [[False] * M for _ in range(0, N)]
    for r in range(0, N):
        for c in range(0, M):
            if MAP[r][c] == 2:
                visited[r][c] = True
                que.append((r, c, 0))
                flag = True
                break
        if flag:
            break
    
    target = [3, 4, 5]
    while que:
        row, col, path = que.popleft()

        if MAP[row][col] in target:
            return path

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
                continue
            if MAP[next_row][next_col] == 1:
                continue
            if visited[next_row][next_col]:
                continue
            visited[next_row][next_col] = True
            que.append((next_row, next_col, path+1))
    return -1

# N행 M열
N, M = map(int, sys.stdin.readline().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, sys.stdin.readline().rstrip()))

answer = bfs()
if answer == -1:
    print("NIE")
else:
    print("TAK")
    print(answer)