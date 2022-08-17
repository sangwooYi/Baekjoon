import sys
sys.stdin = open("baek16929.txt")

"""
dfs 기초문제!
"""

def dfs(arr, start_row, start_col, now_row, now_col, path, visited):
    global is_possible

    alph = arr[start_row][start_col]
    r = len(arr)
    c = len(arr[0])

    for i in range(0, 4):
        next_row = now_row + dr[i]
        next_col = now_col + dc[i]
        
        if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
            continue
        if arr[next_row][next_col] != alph:
            continue

        if visited[next_row][next_col]:
            if path >= 4 and next_row == start_row and next_col == start_col:
                is_possible = True
                return
            continue
        visited[next_row][next_col] = True
        dfs(arr, start_row, start_col, next_row, next_col, path+1, visited)
        visited[next_row][next_col] = False
            



N, M = map(int, input().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

is_possible = False
for i in range(0, N):
    for j in range(0, M):
        if not is_possible:
            check = [[False] * M for _ in range(0, N)]
            check[i][j] = True
            dfs(MAP, i, j, i, j, 1, check)
if is_possible:
    print("Yes")
else:
    print("No")