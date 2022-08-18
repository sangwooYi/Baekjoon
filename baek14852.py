N = int(input())


mod = 1000000007
DP = [0] * (N+2)
DP[0] = 1
DP[1] = 2
DP[2] = 7

for i in range(3, N+1):
    DP[i] = (DP[i-1]*3 + DP[i-2] - DP[i-3]) % mod
print(DP[N] % mod)
