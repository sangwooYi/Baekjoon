import sys
from collections import deque
sys.stdin = open("baek23747.txt")


def setup_ward(start_row, start_col):

    visited[start_row][start_col] = "."
    que = deque()
    que.append((start_row, start_col))
    cur_char = MAP[start_row][start_col]
    while que:
        row, col = que.popleft()

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= R or next_col >= C:
                continue
            if visited[next_row][next_col] == ".":
                continue
            if MAP[next_row][next_col] != cur_char:
                continue
            visited[next_row][next_col] = "."
            que.append((next_row, next_col))


# U, D, L, R
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
dir_dict = {"U": 0, "D": 1, "L": 2, "R": 3}
R, C = map(int, sys.stdin.readline().split())

# 시야 없으면 #, 있으면 .
visited = [["#"] * C for _ in range(0, R)]
MAP = [0] * R
for i in range(0, R):
    MAP[i] = list(sys.stdin.readline().rstrip())

HR, HC = map(int, sys.stdin.readline().split())
operators = list(sys.stdin.readline().rstrip())

# 경로가 맵을 벗어나는 경우는 없음
cur_row, cur_col = HR-1, HC-1
for operator in operators:
    # 와드 설치시, 인접한 같은 알파벳은 전부 체크하므로, 이미 방문한 상태면 굳이 작업 X
    if operator == "W":
        if visited[cur_row][cur_col] != ".":
            setup_ward(cur_row, cur_col)
    # "W" 외에는 방향 인자임
    else:
        cur_dir = dir_dict[operator]
        
        cur_row += dr[cur_dir]
        cur_col += dc[cur_dir]

visited[cur_row][cur_col] = "."

for d in range(0, 4):
    next_row = cur_row + dr[d]
    next_col = cur_col + dc[d]
    if next_row < 0 or next_col < 0 or next_row >= R or next_col >= C:
        continue
    visited[next_row][next_col] = "."

for r in range(0, R):
    print("".join(visited[r]))