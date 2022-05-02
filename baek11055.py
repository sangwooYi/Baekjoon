import sys
sys.stdin = open("baek11055.txt")

"""
LCS 9251번
LIS 11053, 11055번
이 DP 유형도 꼭 기억하자!
"""

N = int(input())
A = list(map(int, input().split()))
DP = [A[i] for i in range(0, N)]

for i in range(1, N):
    for j in range(0, i):
        # 증가 수열일 때 적절한 작업을 하면 됨
        if A[j] < A[i]:
            DP[i] = max(DP[i], DP[j]+A[i])
print(max(DP))