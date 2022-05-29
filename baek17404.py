import sys
sys.stdin = open("baek17404.txt")

"""
조건
2 ~ N-1 까지는 양 옆의 집과 색깔이 달라야한다.
1번 집은 2번집과 N번집이랑 달라야 한다.
N번집은 N-1번집과 1번집과 색이 달라야 한다.

DP[a][b]
b는 0 빨 / 1 초  / 2 파
a는 현재 집의 위치
즉 a번째 집을 특정 색깔로 칠할때까지의 총 최소비용

얘는 1149번 문제와 다르게 처음과 마지막 집도 서로 색이 달라야한다.
따라서 첫번쨰 집에 대한 정보를 갖고 있어야 할듯??
=> 첫번쨰 집 색을 정해두고 시작해야 된다!

헷갈리지말자... 그냥 양옆의 집이랑만 색이 다르면된다.
즉 R-G-R 이래도 상관없는것!
따라서, 바로 직전칸에서 부터 체크하면 됨!
따라서 이게 점화식이 된다
DP[i][R] = min(DP[i-1][G], DP[i-1][B]) + costs[i][R]
여기서 이문제는
첫번째 집 사용을 강제하면 됨
+ 마지막 집에 대한 비용을 체크할 때 첫번째 집과 다른 경우를 전부 체크
즉 total 6가지의 Case가 나오게 되는것!
"""


N = int(input())
costs = [0] * N
for i in range(0, N):
    costs[i] = list(map(int, input().split()))

INF = 987654321

answer = INF
# 첫번째 집 색깔을 가정하고 시작
for i in range(0, 3):
    DP = [[0] * 3 for _ in range(0, N)]
    # 초깃값 세팅, 무조건 첫번째 집을 강제 해야하므로 이렇게 세팅해야한다.
    for j in range(0, 3):
        if i != j:
            DP[0][j] = INF
        else:
            DP[0][j] = costs[0][j]
    for j in range(1, N):
        DP[j][0] = min(DP[j-1][1], DP[j-1][2]) + costs[j][0]
        DP[j][1] = min(DP[j-1][0], DP[j-1][2]) + costs[j][1]
        DP[j][2] = min(DP[j-1][0], DP[j-1][1]) + costs[j][2]
    
    for j in range(0, 3):
        # 시작집과 다른 경우만
        if i != j:
            temp = DP[N-1][j]
            if temp < answer:
                answer = temp
print(answer)
