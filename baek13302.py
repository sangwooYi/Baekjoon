import sys
sys.stdin = open("baek13302.txt")

"""
1일권 10000원
3일권 25000원 쿠폰1장
5일권 37000원 쿠폰2장

DP[i][j] i 날짜에 j장 쿠폰을 갖고 있는 최소 금액

bottom - up 방식!
반드시 다시 풀어 보자!
+ 문제 잘 읽자
다시 풀 문제!
"""


N, M = map(int, input().split())
if M > 0:
    days = list(map(int, input().split()))
else:
    days = []
INF = 987654321
# 100일째에 5일권 사용하는 경우도 있으므로 105까지가 범위여야함
DP = [[INF] * 106 for _ in range(0, 106)]
DP[0][0] = 0

# 최대 쿠폰 수령 갯수는 100//5 == 20*2 40장(반드시 쿠폰을 쓸 필요는 없다!)
for i in range(0, N+1):
    for j in range(0, 40):
        if DP[i][j] == INF:
            continue
        res = DP[i][j]
        # 다음날이 안가는 날인 경우
        if i+1 in days:
            # 안가니까 그냥 이렇게 다음날 그대로
            DP[i+1][j] = min(res, DP[i+1][j])
        if j >= 3:
            # 쿠폰이 3장 이상이면 다음날은 공짜로 가능 (반드시 쿠폰을 쓸 필요는 없다)
            DP[i+1][j-3] = min(res, DP[i+1][j-3])
        # 1일권
        DP[i+1][j] = min(DP[i+1][j], res+10000)
        # 3일권 1 ~ 3일 안에서 자유롭다
        for k in range(1, 4):
            DP[i+k][j+1] = min(DP[i+k][j+1], res+25000)
        k = 0
        # 5일권 역시 1일 ~ 5일안에서 자유롭다
        for k in range(1, 6):
            DP[i+k][j+2] = min(DP[i+k][j+2], res+37000)
print(min(DP[N]))
