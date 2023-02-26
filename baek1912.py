import sys
sys.stdin = open("baek1912.txt")

"""
DP의 핵심은 메모이제이션 or 점화식!
DP[N] 은 N번째까지의 최대 연속합
점화식을 세우는게 항상 핵심이다!

여기선
DP[N] = max(DP[n-1]+arr[n], arr[n])
직전합이 음수라면, 그냥 arr[n]이 최댓값이 됨. 아니라면 연속합이 최대
"""

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

DP = [0] * N
DP[0] = nums[0]
for i in range(1, N):
    DP[i] = max(DP[i-1]+nums[i], nums[i])
print(max(DP))