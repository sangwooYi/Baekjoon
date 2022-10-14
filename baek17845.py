import sys
sys.stdin = open("baek17845.txt")


"""
DP[a][b]
a번쨰까지 b 시간을 할애했을때 뽑아낼수있는 최대 중요도
4795번같은 경우는, 한가지 종류가 무제한으로 있는 경우,
이번 경우난 한 과목은 한번만 처리할 수 있다!
"""

N, K = map(int, input().split())
subjects = [0] * K
for i in range(0, K):
    I, T = map(int, input().split())
    subjects[i] = (I, T)
DP = [[0] * (N+1) for _ in range(0, K+1)]


# 수량이 정해진 배낭문제는 이렇게 접근해야 한다!
for i in range(0, K):
    importance, req_time = subjects[i]
    for j in range(1, N+1):
        if j >= req_time:
            # 해당문제를 풀수는 있는데, 풀때 / 안풀 때 중 최댓값 (이부분이 중요하다!)
            DP[i+1][j] = max(DP[i][j], DP[i][j-req_time]+importance)
        else:
            # 안푼다.
            DP[i+1][j] = DP[i][j]
print(max(DP[K]))
