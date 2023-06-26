import sys
sys.stdin = open("baek15645.txt")


N = int(sys.stdin.readline().rstrip())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, sys.stdin.readline().split()))

INF = 987654321
MAX_DP = [[0] * 3 for _ in range(0, N)]
MIN_DP = [[INF] * 3 for _ in range(0, N)]

for i in range(0, 3):
    MAX_DP[0][i] = MAP[0][i]
    MIN_DP[0][i] = MAP[0][i]

for i in range(1, N):
    MAX_DP[i][0] = max(MAX_DP[i][0], MAX_DP[i-1][0]+MAP[i][0], MAX_DP[i-1][1]+MAP[i][0])
    MIN_DP[i][0] = min(MIN_DP[i][0], MIN_DP[i-1][0]+MAP[i][0], MIN_DP[i-1][1]+MAP[i][0])

    MAX_DP[i][1] = max(MAX_DP[i][1], MAX_DP[i-1][0]+MAP[i][1], MAX_DP[i-1][1]+MAP[i][1], MAX_DP[i-1][2]+MAP[i][1])
    MIN_DP[i][1] = min(MIN_DP[i][1], MIN_DP[i-1][0]+MAP[i][1], MIN_DP[i-1][1]+MAP[i][1], MIN_DP[i-1][2]+MAP[i][1])

    MAX_DP[i][2] = max(MAX_DP[i][2], MAX_DP[i-1][1]+MAP[i][2], MAX_DP[i-1][2]+MAP[i][2])
    MIN_DP[i][2] = min(MIN_DP[i][2], MIN_DP[i-1][1]+MAP[i][2], MIN_DP[i-1][2]+MAP[i][2])        

max_ans = max(MAX_DP[N-1])
min_ans = min(MIN_DP[N-1])
print(f"{max_ans} {min_ans}")