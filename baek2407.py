"""
그냥 factorial 
메모이제이션 이용해서 만들고
=> (n!)/(n-r)!*r! 을 직접 계산하자
"""

def factorial(n):
    if n < len(DP):
        return DP[n]
    start = len(DP)
    for i in range(start, n+1):
        DP.append(i*DP[i-1])
    return DP[n]



N, M = map(int, input().split())
DP = [1, 1]
a = factorial(N)
b = factorial(N-M)
c = factorial(M)

answer = a // (b*c)
print(answer)