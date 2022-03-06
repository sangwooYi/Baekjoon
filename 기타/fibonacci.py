import sys
sys.stdin = open("fibonacci.txt")

"""
무조건 메모이제이션!!!
메모이제이션 + DP 연습좀 해둬야함
"""

def fibonacci(n):
    DP = [0, 1]
    if n < 2:
        return DP[n]
    for i in range(2, n+1):
        DP.append(DP[i-1] + DP[i-2])
    return DP[n]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    z_count = 0
    o_count = 0
    if N == 0:
        z_count = 1
        o_count = 0
    elif N == 1:
        z_count = 0
        o_count = 1
    else:
        z_count = fibonacci(N-1)
        o_count = fibonacci(N)

    print(z_count, o_count)
