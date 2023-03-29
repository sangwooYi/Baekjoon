N = int(input())
nums = list(map(int, input().split()))
DP = [1] * N

for i in range(0, N-1):
    for j in range(i+1, N):
        if nums[i] < nums[j]:
            DP[j] = max(DP[j], DP[i]+1)

print(max(DP))