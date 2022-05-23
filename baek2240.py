import sys
sys.stdin = open("baek2240.txt")

"""
전략.
시작은 1번나무에서부터 시작
W 최대 이동횟수이므로
0 ~ W까지 전부 탐색해야함

그리고 움직일때 시간은 무시함 즉 0초부터 움직인채로 시작할수도있고,
움직이는데 추가 시간 X

DP[a][b]  a초일때 b번움직여서 얻을 수 있는 최대 자두 값
움직인 횟수가 짝수 => 1번 홀수 => 2번나무  이용 2차원 리스트로 해결 가능

총 경우는 3가지이다
1번 나무에서 자두가 떨어지고 그 위치에 있는경우

2번 나무에서 자두가 떨어지고 그 위치에 있는경우

자두를 못 먹는 경우

각 모든 경우는, 이전에 이미 이동해있는경우 / 현재 초에 맞추어서 이동하는 경우 2가지씩으로 분기된다
DP[i][j] = max(DP[i-1][j], DP[i-1][j-1]) + 1
못먹으면 그냥
DP[i][j] = max(DP[i-1][j], DP[i-1][j-1])

DP는 점화식을 엄밀하게 세우는것이 핵심이다!!
"""

T, W = map(int, input().split())
# t 초에 어디서 자두가 떨어지는지 체크
# DP[a][b] 는 b번 움직여서 a 초상황에서 얻은 최대 자두 갯수
plums = [0] * T
for i in range(0, T):
    plums[i] = int(input())
# 이동횟수 0 ~ W까지 탐색
DP = [[0] * (W+1) for _ in range(0, T)]

for i in range(0, T):
    # 아예 안움직일때 값 세팅
    if plums[i] == 1:
        DP[i][0] = DP[i-1][0] + 1
    else:
        DP[i][0] = DP[i-1][0]   

    # 매초마다 모든 이동횟수를 (j == i까지) 탐색하며 총 3가지 경우가 있다., 매초마다 모든 이동 횟수를 시행한다.
    for j in range(1, W+1):
        # 어차피 1초에 1번씩 이동하는것 이상의 의미는 없다. (근데 이 조건 없어도 풀린다.)
        if j > i:
            break
        # 현재 1번나무에서 떨어지고 1번나무에 있는 경우, 이동횟수가 짝수
        if plums[i] == 1 and j % 2 == 0:
            # 이전부터 옮겨졌거나, 해당 초에 옮기거나, 이동횟수가 홀수
            DP[i][j] = max(DP[i-1][j], DP[i][j-1]) + 1
        elif plums[i] == 2 and j % 2 == 1:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-1]) + 1
        # 그냥 못먹는 상황
        else:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-1])

answer = 0
for i in range(0, W+1):
    if DP[T-1][i] > answer:
        answer = DP[T-1][i]
print(answer)