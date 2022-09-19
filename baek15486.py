import sys
sys.stdin = open("baek15486.txt")

"""
dn = 현재 날짜
dn + (ti-1) < N 이어야 한다.

# DP[i-1] 부분에 아무 값이 안들어오는 경우가 존재한다.
이런 경우를 대비해서 그 이전까지의 최댓값을 계속 저장 하는 것.
max_now = max(max_now, DP[i-1]) 부분이 들어가야 하며,
비교도 DP[i-1+ti] = max(DP[i-1+ti], max_now+pi) 가 되어야 한다.

이 두 포인트를 놓쳤음!
"""


N = int(input())
schedules = [0] * N
for i in range(0, N):
    term, cost = map(int, input().split())
    schedules[i] = (term, cost)
DP = [0] * (N+1)

max_now = 0
for i in range(1, N+1):
    ti, pi = schedules[i-1]
    # 이부분이 핵심이다!, DP[N] 은 N일까지의 최댓값이 저장되어 있어야 함!!
    max_now = max(max_now, DP[i-1])
    if i + ti - 1 <= N:
        DP[i+ti-1] = max(DP[i+ti-1], max_now+pi)

print(max(DP))
