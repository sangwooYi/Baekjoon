import sys
sys.stdin = open("baek11054.txt")

"""
최댓값이 기준이 아닌게 최대 수열이 될 수 있따!

ex)
1 5 2 3 4 3 2 1
3중 for문 10억번... 가능하려나
C언어 기준으로 10억회 연산이 1초정도라고 하긴 했음

좀더 나은 풀이도 존재!
100만 * 3 연산으로 풀 수 있다!
"""


N = int(input())
A = list(map(int, input().split()))
# 증가
LIS = [1] * N
# 감소
LDS = [1] * N

# 정방향
for i in range(0, N):
    for j in range(0, i):
        if A[j] < A[i]:
            LIS[i] = max(LIS[i], LIS[j]+1)

# 역방향
for i in range(N-1, -1, -1):
    for j in range(N-1, i-1, -1):
        if A[j] < A[i]:
            LDS[i] = max(LDS[i], LDS[j]+1)
answer = 0
for i in range(0, N):
    temp = LIS[i] + LDS[i] - 1
    if answer < temp:
        answer = temp
print(answer)
    


# 3중 for 문 (얘도 풀리긴 함)
# for i in range(0, N):
#     DP = [1] * N
#     for j in range(1, i+1):
#         for k in range(0, j):
#             if A[k] < A[j]:
#                 DP[j] = max(DP[j], DP[k]+1)
#     for j in range(i+1, N):
#         for k in range(i, j):
#             if A[k] > A[j]:
#                 DP[j] = max(DP[j], DP[k]+1)
#     temp = max(DP)
#     if answer < temp:
#         answer = temp
# print(answer)


