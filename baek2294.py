import sys
sys.stdin = open("baek2294.txt")

"""
얘는 최소의 갯수를 찾는 것!

여기서 DP[i] 는 i가치를 만드는데 필요한 최소 동전의 갯수!
"""

N, K = map(int, input().split())
coins = [0] * N
DP = [100001] * (K+1)
DP[0] = 0
for i in range(0, N):
    tmp = int(input())
    coins[i] = tmp

for i in range(0, len(coins)):
    w = coins[i]
    for j in range(w, K+1):
        # 현재 값 vs DP[j-w]에서 w 가치의 동전 한개를 쓴 경우 중 최소 갯수를 사용한 값을 갱신
        DP[j] = min(DP[j], DP[j-w]+1)

if DP[K] == 100001:
    print(-1)
else:
    print(DP[K])
