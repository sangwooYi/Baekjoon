import sys
sys.stdin = open("baek11053.txt")
"""
DP 왜이렇게 어렵냐 ㅠㅠ
LIS (Longest Increasing Subsequences)
LCS (Longest Common Subsequences) 두개가 유명한 DP 문제다 둘다 익혀둘것!
"""

N = int(input())
A = list(map(int, input().split()))

# 자기 자신은 무조건 포함
DP = [1] * N
for i in range(1, N):
    for j in range(0, i):
        # 어쨌건 j번째숫자보다 i 번째숫자가 크면
        if A[j] < A[i]:
            # 이런 논리를 혼자서 할 수 있어야하는데..
            # 현재 DP에 저장된 값 or DP[j]에서 1개 증가 중 큰값에 해당하는 길이가 최장수열이 된다.
            DP[i] = max(DP[i], DP[j]+1)
print(max(DP))