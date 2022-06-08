import sys
sys.stdin = open("baek2293.txt")
"""
얘는 경우의 수!
"""


N, K = map(int, input().split())
coins = [0] * N
DP = [0] * (K+1)
# 초기화를 이렇게 해야한다... 1개만 쓰는 경우 체크용
DP[0] = 1
for i in range(0, N):
    tmp = int(input())
    coins[i] = tmp
coins.sort()


for i in range(0, len(coins)):
    w = coins[i]
    for j in range(w, K+1):
        DP[j] += DP[j-w]

print(DP[K])
