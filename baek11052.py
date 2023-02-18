import sys
sys.stdin = open("baek11052.txt")

"""
DP[K] 
K개를 사는데 들어가는 최대금액

DP를 푸는 핵심은 항상 DP를 어떻게 설계할것인가임!

"""

N = int(input())
card_infos = list(map(int, input().split()))


DP = [0] * (N+1)

for k in range(1, N+1):
    for i in range(0, N):
        c_num = i+1
        if k >= c_num:
            DP[k] = max(DP[k], DP[k-c_num]+card_infos[i])
print(DP[N])