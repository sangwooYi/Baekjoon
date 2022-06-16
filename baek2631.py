import sys
sys.stdin = open("baek2631.txt")

"""
얘는 그냥 최장증가수열만 찾아도 되는문제

7570번이랑 비교하자!
(7570번은 매번 바로 앞, 바로 뒤로만 보낼 수 있어서 '연속한' 최장수열을 찾아야 했었다.)
"""

N = int(input())
numbers = [0] * N
for i in range(0, N):
    numbers[i] = int(input())

# DP[i] i번째까지에서의 최장수열 (기본값은 1이다)
DP = [1 for _ in range(0, N+1)]

# 기준이 i 인덱스 값
for i in range(1, N):
    # 비교대상은 0 ~ i-1 인덱스까지
    for j in range(0, i):
        # 일단 j번 값 < i번 값이면
        if numbers[j] < numbers[i]:
            # 현재 저장된 값 vs DP[j] + 1 중 큰값을 선택 
            DP[i] = max(DP[i], DP[j]+1)
ans = max(DP)
print(N-ans)