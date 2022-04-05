"""
이 문제는
N-1 에서 1짜리 1개 놓는 경우
N-2 에서 1*2 짜리 2개 or 2*2짜리 1개 놓는 경우
DP[N] = DP[N-1] + 2*DP[N-2]

"""

def dfs(n):
    if n <= 2:
        return DP[n]
    
    for i in range(3, n+1):
        DP.append(DP[i-1] + 2*DP[i-2])
    return (DP[n] % 10007)

N = int(input())
DP = [0, 1, 3]
ans = dfs(N)
print(ans)