N = int(input())
nums = list(map(int, input().split()))

DP = [0] * N
for i in range(0, N):
    DP[i] = nums[i]

for i in range(1, N):
    for j in range(0, i):
        if nums[j] > nums[i]:
            DP[i] = max(DP[i], DP[j]+nums[i])
print(max(DP))