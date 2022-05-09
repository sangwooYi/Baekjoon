import sys
sys.stdin = open("baek9084.txt")

"""
이거 왜이렇게 이해가 안가냐 ㅡㅡ
"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    coins = list(map(int, input().split()))
    target = int(input())
    DP = [0] * (target+1)
    DP[0] = 1
    for i in range(0, len(coins)):
        coin = coins[i]
        for j in range(coin, target+1):
            DP[j] += DP[j-coin]
    print(DP[target])