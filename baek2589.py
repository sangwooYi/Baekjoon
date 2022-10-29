import sys
from collections import deque
sys.stdin = open("baek2589.txt")


def calc_treasures_path(arr):

    r = len(arr)
    c = len(arr[0])

    land = "L"
    sea = "W"

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    max_path = 0

    tmp_que = deque()
    for row in range(0, r):
        for col in range(0, c):
            if arr[row][col] == land:
                tmp_que.append((row, col))

    while tmp_que:
        start_row, start_col = tmp_que.popleft()
        visited = [[False] * c for _ in range(0, r)]
        visited[start_row][start_col] = True
        que = deque()
        que.append((start_row, start_col, 0))

        tmp_max = 0
        while que:
            row, col, path = que.popleft()

            for d in range(0, 4):
                next_row = row + dr[d]
                next_col = col + dc[d]

                if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
                    continue
                if arr[next_row][next_col] == sea:
                    continue
                if visited[next_row][next_col]:
                    continue
                next_path = path+1
                tmp_max = max(tmp_max, next_path)
                visited[next_row][next_col] = True
                que.append((next_row, next_col, next_path))
        max_path = max(max_path, tmp_max)
    return max_path


R, C = map(int, input().split())
MAP = [0] * R
for i in range(0, R):
    MAP[i] = list(input())

answer = calc_treasures_path(MAP)
print(answer)
