import sys
sys.stdin = open("baek9184.txt")


"""
메모이제이션!
"""

limit = 51
dp = [[[-1 for _ in range(0, limit)] for _ in range(0, limit)] for _ in range(0, limit)]
def baek9184(a, b, c):
    
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if dp[a][b][c] != -1:
        return dp[a][b][c]
    if a > 20 or b > 20 or c > 20:
        dp[a][b][c] = baek9184(20, 20, 20)
        return dp[a][b][c]

    if a < b  and b < c:
        dp[a][b][c] = baek9184(a, b, c-1) + baek9184(a, b-1, c-1) - baek9184(a, b-1, c)
        return dp[a][b][c]

    else:
        dp[a][b][c] = baek9184(a-1, b, c) + baek9184(a-1, b-1, c) + baek9184(a-1, b, c-1)-baek9184(a-1, b-1, c-1)
        return dp[a][b][c]

while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break
    ans = baek9184(a, b, c)
    print(f"w({a}, {b}, {c}) = {ans}")
