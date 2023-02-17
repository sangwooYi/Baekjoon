import sys
sys.stdin = open("baek1303.txt")
from collections import deque

def check_area(start_row, start_col, force):
    
    visited[start_row][start_col] = True
    que = deque()
    que.append((start_row, start_col))

    area = 1
    while que:
        row, col = que.popleft()

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= M or next_col >= N:
                continue
            if not visited[next_row][next_col] and MAP[next_row][next_col] == force:
                visited[next_row][next_col] = True
                que.append((next_row, next_col))
                area += 1
    return area**2

    


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
ALLY = "W"
ENEMY = "B"
# 가로 , 세로
N, M = map(int, input().split())
MAP = [0] * M

for i in range(0, M):
    MAP[i] = list(input())

our_force = 0
enemy_force = 0
visited = [[False] * N for _ in range(0, M)]
for i in range(0, M):
    for j in range(0, N):
        if not visited[i][j]:
            force = MAP[i][j]
            area_power = check_area(i, j, force)

            if force == ALLY:
                our_force += area_power
            else:
                enemy_force += area_power

print(f"{our_force} {enemy_force}")