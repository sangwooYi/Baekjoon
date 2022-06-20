import sys
sys.stdin = open("baek14728.txt")

"""
한 단원 문제는 한번만 풀 수 있다!
따라서
DP[i][j] 로 접근해야함
i번째 물건까지 j 무게로 담았을 때의 최대의 가치

배낭문제 유형 나오면 꼭 풀 수 있어야 한다!
"""

N, T = map(int, input().split())
problems = [0] * N
for i in range(0, N):
    problems[i] = list(map(int, input().split()))

DP = [[0] * (T+1) for _ in range(0, N)]

for i in range(0, N):
    time, score = problems[i]
    for j in range(1, T+1):
        # 담을 수 있는 경우는 현재 물건을  안담는 경우, 담는 경우중 최댓값 선택
        if time <= j:
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-time]+score)
        else:
            DP[i][j] = DP[i-1][j]
print(DP[N-1][T])