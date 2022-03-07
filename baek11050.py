"""
nCk = n! /((n-k)! * k!)
"""

def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial(n - 1)


N, K = map(int, input().split())

answer = factorial(N) // (factorial(K) * factorial(N-K))
print(answer)