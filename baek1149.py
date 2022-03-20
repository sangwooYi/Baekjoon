import sys
sys.stdin = open("baek1149.txt")

"""
이 문제는 조만간 한번 더 풀어보자
"""


N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))
DP = [[0] * 3 for _ in range(0, N)]
DP[0][0] = MAP[0][0]
DP[0][1] = MAP[0][1]
DP[0][2] = MAP[0][2]

for i in range(1, N):
    # 현재 위치를 R로 칠하는 경우  (그 전의 집까지 칠해진 가격에서 G일때 , B일때중 최솟값에다가 현재 집 위치값 더하기)
    DP[i][0] = min(DP[i-1][1], DP[i-1][2]) + MAP[i][0]
    # 현재 위치를 G로 칠하는 경우
    DP[i][1] = min(DP[i-1][0], DP[i-1][2]) + MAP[i][1]
    # 현재 위치를 B로 칠하는 경우
    DP[i][2] = min(DP[i-1][0], DP[i-1][1]) + MAP[i][2]

ans = min(DP[N-1][0], DP[N-1][1], DP[N-1][2])
print(ans)
