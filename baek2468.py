import sys
sys.stdin = open("baek2468.txt")
from collections import deque


def bfs(start_row, start_col):
    visited[start_row][start_col] = True

    que = deque()
    que.append((start_row, start_col))

    while que:
        row, col = que.popleft()
        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                continue
            if visited[next_row][next_col]:
                continue
            visited[next_row][next_col] = True
            que.append((next_row, next_col))


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))

min_height = 100
# max_height 이하가 잠긴다면 그냥 사실상 다 잠기는것.
max_height = 1
for i in range(0, N):
    for j in range(0, N):
        num = MAP[i][j]
        max_height = max(max_height, num)
        min_height = min(min_height, num)

# 결국 아무도 안잠겼을때 안전영역갯수가 1이다.
max_area = 1

# 아무도 안잠길때를 기본으로 시작
rain_fall = min_height-1
# 어차피 max_height까지 차오르면 영역이 0이되어버린다.
while rain_fall < max_height:
    visited = [[False] * N for _ in range(0, N)]

    for i in range(0, N):
        for j in range(0, N):
            num = MAP[i][j]
            # 해당 높이 이하는 전부 잠기는 것
            if num <= rain_fall:
                visited[i][j] = True
    area = 0
    for i in range(0, N):
        for j in range(0, N):
            if not visited[i][j]:
                area += 1
                bfs(i, j)
    max_area = max(max_area, area)

    rain_fall += 1

print(max_area)