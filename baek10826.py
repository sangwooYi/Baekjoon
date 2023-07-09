import sys
sys.setrecursionlimit(10**5)

N = int(input())


def fibo(n):

    if len(number) > n:
        return number[n]
    else:
        cur = fibo(n-1)+fibo(n-2)
        number.append(cur)
        return cur

number = [0, 1]
ans = fibo(N)
print(ans)