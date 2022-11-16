import sys
sys.stdin = open("baek2225.txt")

"""
DP[K][N]

K 개 숫자를 써서 N을 만드는 경우를 구하기!

K / N 둘다 최대 200까지라서 충분히 가능
"""

N, K = map(int, input().split())

DP = [[0] * (N+1) for _ in range(0, K+1)]

# 초깃값 세팅
for i in range(0, N+1):
    DP[1][i] = 1
     
for i in range(2, K+1):
    for j in range(0, N+1):
        for k in range(0, j+1):
            DP[i][j] += DP[i-1][j-k]

print(DP[K][N]%1000000000)