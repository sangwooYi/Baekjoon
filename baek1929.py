import sys
sys.stdin = open("baek1929.txt")


"""
2, 3 을 미리 저장해두고
이후부터는 홀수만 체크 

특정 값이 소수라고 판단방법
prime 배열에 있는 값들로 나누어지는지 체크,
prime[i] ** 2 <= 현재 판단하려는수 까지만 체크하면 된다!

"""

def find_prime(n):
    # 2, 3은 미리 넣어둔다.
    primes = [2, 3]

    for i in range(5, n+1, 2):
        flag  = False
        for j in range(0, len(primes)):
            # 종료조건 1. 현재 보려는 소수의 제곱값이 i를 넘었을때 2. 나누어 떨어질떄
            if primes[j] ** 2 > i:
                break
            if i % primes[j] == 0:
                flag = True
                break
        if not flag:
            primes.append(i)
    return primes




M, N = map(int, input().split())
answer = find_prime(N)
for i in range(0, len(answer)):
    if answer[i] < M:
        continue
    # M , N 이 1, 2로 주어졌을때 처리를 위함
    if answer[i] > N:
        continue
    print(answer[i])
