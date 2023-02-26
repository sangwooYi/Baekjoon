import sys
sys.stdin = open("baek11048.txt")


N, M = map(int, sys.stdin.readline().split())
MAP = [0] * N
DP = [[0] * M for _ in range(0, N)]
for i in range(0, N):
    MAP[i] = list(map(int, sys.stdin.readline().split()))

DP[0][0] = MAP[0][0]
for row in range(0, N):
    for col in range(0, M):
        if row == 0:
            if col == 0:
                continue
            DP[row][col] = max(DP[row][col], DP[row][col-1]+MAP[row][col])
        elif col == 0:
            DP[row][col] = max(DP[row][col], DP[row-1][col]+MAP[row][col])
                   
        else:
            DP[row][col] = max(DP[row][col], DP[row-1][col]+MAP[row][col], DP[row][col-1]+MAP[row][col], DP[row-1][col-1]+MAP[row][col])
print(DP[N-1][M-1])

