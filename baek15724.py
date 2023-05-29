import sys
sys.stdin = open("baek15724.txt")

N, M = map(int, sys.stdin.readline().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, sys.stdin.readline().split()))

# 부분합 구하기
sum_arr = [[0] * M for _ in range(0, N)]
for r in range(0, N):
    for c in range(0, M):
        if c == 0:
            sum_arr[r][c] = MAP[r][c]
        else:
            sum_arr[r][c] = sum_arr[r][c-1]+MAP[r][c]

for c in range(0, M):
    for r in range(1, N):
        sum_arr[r][c] += sum_arr[r-1][c]

K = int(sys.stdin.readline().rstrip())
for _ in range(0, K):
    # x가 행 y가 열
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    
    cur_area = sum_arr[x2][y2]

    if x1 > 0:
        cur_area -= sum_arr[x1-1][y2]
    if y1 > 0:
        cur_area -= sum_arr[x2][y1-1]
    if x1 > 0 and y1 > 0:
        cur_area += sum_arr[x1-1][y1-1]
    print(cur_area)