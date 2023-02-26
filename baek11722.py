import sys
sys.stdin = open("baek11722.txt")


"""
DP[N]  N번쨰까지 보았을떄 가장 긴 감소하는 부분순열

O(N**2) 으로할떄는 이러헤
"""

N = int(input())
nums = list(map(int, input().split()))
DP = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if nums[j] > nums[i]:
            DP[i] = max(DP[i], DP[j]+1)
print(max(DP))