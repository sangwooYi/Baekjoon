import sys
sys.stdin = open("baek10709.txt")


H, W = map(int, input().split())
MAP = [0] * H
for i in range(0, H):
    MAP[i] = list(input())


visited = [[-1] * W for _ in range(0, H)]

arr = []
for r in range(0, H):
    for c in range(0, W):
        if MAP[r][c] == "c":
            visited[r][c] = 0
            arr.append((r, c, 0))

while arr:
    tmp_arr = []
    for i in range(0, len(arr)):
        row, col, path = arr.pop()
        # 매번 동쪽으로
        next_row = row
        next_col = col+1

        if next_col >= W:
            continue
        # 아직 안지난 경우만
        if visited[next_row][next_col] == -1:
            visited[next_row][next_col] = path+1
            tmp_arr.append((next_row, next_col, path+1))
    arr = tmp_arr

for i in range(0, H):
    print(" ".join(map(str, visited[i])))