import sys
sys.stdin = open("baek1890.txt")


N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))
DP = [[0] * N for _ in range(0 ,N)]
DP[0][0] = 1

dr = [1, 0]
dc = [0, 1]
for row in range(0, N):
    for col in range(0, N):
        if row == N-1 and col == N-1:
            continue
        term = MAP[row][col]

        for d in range(0, 2):
            next_row = row + dr[d]*term
            next_col = col + dc[d]*term

            if next_row >= N or next_col >= N:
                continue
            DP[next_row][next_col] += DP[row][col]
print(DP[N-1][N-1])
