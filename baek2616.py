from itertools import accumulate
import sys
sys.stdin = open("baek2616.txt")

"""
전략 1.

DP[a][b] a 번열차를 b번 객실까지 선택할때의 누적합

DP 좀 더 열심히 풀자
꼭 다시 풀어볼 것
기본적으로 accum[a]  (0 ~ a-1 인덱스까지의 총합) 을 구한다
accum[5] - accum[2] 이면  3번인덱스 + 4번인덱스의 합을 구할 수 는것
(즉 누적합을 이용해서 구간합을 바로 구할 수 있다!)
=> 이부분이 핵심

여기서 accum[b] - accum[b-K] 를 하면 b-K+1 ~ b인덱스까지 K칸의 구간합이 나오는것

                            # 이부분이 점화식세우기 어려웠다.
DP[a][b] = max(DP[a][b-1], DP[a-1][b-K] + accum[b] - accum[b-K])

DP는 점화식 or 메모이제이션이다!!
"""

# 열차 칸 수
N = int(input())
rooms = list(map(int, input().split()))

# 한 소형 기관차가 소화할 수 있는 객실 수 소형기관차는 총 3대가 존재
# 항상 K는 1/3*N 보다 작은 값을 갖는다. (즉 항상 3대가 전부 활용 됨)
K = int(input())

# 구간합
accum = [0] * (N+1)
for i in range(0, N):
    accum[i+1] = accum[i] + rooms[i]


DP = [[0] * (N+1) for _ in range(0, 4)]

# 1부터 3번 기관차
for i in range(1, 4):
    # 구간합은 K*i 칸부터 체크하면 된다.
    for j in range(K*i, N+1):
        if i == 1:
            # j == K*i 일때는 그냥 첫칸부터 j+K-1 까지의 구간합임!
            # j == k*i 일때는 DP[i][j-1]은 여기서 그냥 0인것
            DP[i][j] = max(DP[i][j-1], accum[j] - accum[j-K])
        else:
            DP[i][j] = max(DP[i][j-1], DP[i-1][j-K] + (accum[j]-accum[j-K]))

print(max(DP[3]))