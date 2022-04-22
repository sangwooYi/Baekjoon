import sys
sys.stdin = open("baek9465.txt")
"""
아이디어1.
D[0][a] 의 값은 max(D[1][a-1] + MAP[0][n], D[0][a-2] + MAP[0][n], D[1][a-2] + MAP[0][n])
이 외에는 더 따질것은 없지않나??

그리고 포인트는 무조건 마지막변이아니라
DP[0][N-1], DP[1][N-1] , DP[0][N], DP[1][N] 중에 최댓값이 있다는것!
"""



T = int(sys.stdin.readline())
for tc in range(1, T+1):
    N = int(sys.stdin.readline())
    MAP = [0] * 2
    for i in range(0, 2):
        MAP[i] = list(map(int, sys.stdin.readline().split()))
    DP = [[0] * N for _ in range(0, 2)]

    DP[0][0] = MAP[0][0]
    DP[1][0] = MAP[1][0]
    if N == 1:
        ans = max(DP[0][0], DP[1][0])
    else:
        DP[0][1] = DP[1][0] + MAP[0][1]
        DP[1][1] = DP[0][0] + MAP[1][1]
        if N == 2:
            ans = max(DP[0][1], DP[1][1])
        else:
            for i in range(2, N):
                DP[0][i] = max(DP[1][i-1], DP[0][i-2], DP[1][i-2]) + MAP[0][i]
                DP[1][i] = max(DP[0][i-1], DP[0][i-2], DP[1][i-2]) + MAP[1][i]
        ans = max(DP[0][N-1], DP[1][N-1], DP[0][N-2], DP[1][N-2])
    print(ans)