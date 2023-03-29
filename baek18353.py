import sys
sys.stdin = open("baek18353.txt")

N = int(input())
soldiers = list(map(int, input().split()))

DP = [1] * N

for i in range(0, N-1):
    for j in range(i, N):
        if soldiers[i] >soldiers[j]:
            DP[j] = max(DP[j], DP[i]+1)
print(N-max(DP))