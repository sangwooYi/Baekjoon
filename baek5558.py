import sys
from collections import deque
sys.stdin = open("baek5558.txt")


def bfs(start_row, start_col, target):

    que = deque()
    visited = [[False] * W for _ in range(0, H)]
    visited[start_row][start_col] = True

    que.append((start_row, start_col, 0))
    
    while que:

        row, col, path = que.popleft()

        if MAP[row][col] == target:
            return path

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= H or next_col >= W:
                continue
            if MAP[next_row][next_col] == "X":
                continue
            if visited[next_row][next_col]:
                continue
            visited[next_row][next_col] = True
            que.append((next_row, next_col, path+1))


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

H, W, N = map(int, sys.stdin.readline().split())

factories = [0] * N
chees_kinds = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

MAP = [[0] * W for _ in range(0, H)]

for i in range(0, H):
    MAP[i] = list(sys.stdin.readline().rstrip())

    for j in range(0, len(MAP[i])):
        if MAP[i][j] in chees_kinds:
            factories[int(MAP[i][j])-1] = [i, j]

        if MAP[i][j] == "S":
            s_row = i
            s_col = j

total = 0
for i in range(0, len(factories)):
    target = str(i+1)
    
    if i > 0:
        s_row, s_col = factories[i-1]
    total += bfs(s_row, s_col, target)
print(total)