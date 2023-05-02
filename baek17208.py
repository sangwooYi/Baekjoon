import sys
sys.stdin = open("baek17208.txt")

"""
DP[i][a][b] <= i번째 주문까지 에서
치즈버거 a개, 감자튀김 b개를 사용해서 만들 수 있는 주문의 최대 갯수??

배낭문제!!
"""

N, M, K = map(int, input().split())
orders = [0] * N
for i in range(0, N):
    orders[i] = list(map(int, input().split()))

DP = [[[0 for _ in range(0, K+1)] for _ in range(0, M+1)] for _ in range(0, N+1)]

for i in range(1, N+1):
    burger_cnt, chips_cnt = orders[i-1]

    for j in range(1, M+1):
        for k in range(1, K+1):
            # 해당 주문 못담는다.
            if j < burger_cnt or k < chips_cnt:
                DP[i][j][k] = DP[i-1][j][k]
            else:
                DP[i][j][k] = max(DP[i-1][j][k], DP[i-1][j-burger_cnt][k-chips_cnt]+1)
print(DP[N][M][K])
    