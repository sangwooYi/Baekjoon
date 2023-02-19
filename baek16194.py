import sys
sys.stdin = open("baek16194.txt")

"""
DP[K] 
K개 카드를 살때까지 최소 금액
"""


N = int(input())
card_inofs = list(map(int, input().split()))
INF = 987654321
DP = [INF] * (N+1)
DP[0] = 0

for k in range(1, N+1):
    for i in range(0, N):
        card_num = i+1
        if k-card_num >= 0:
            DP[k] = min(DP[k], DP[k-card_num]+card_inofs[i])
print(DP[N])