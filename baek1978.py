import sys
sys.stdin = open("baek1978.txt")

"""
문제 조건 잘읽자
N 이 0도 된다.
"""


def find_prime(num):
    prime = [2, 3]
    for n in range(5, num+1, 2):
        flag = True
        for i in range(0, len(prime)):
            # prime ** 2 <= n 까지만 보면 된다
            if prime[i] ** 2 > n:
                break
            if (n % prime[i]) == 0:
                flag = False
                break
        if flag:
            prime.append(n)
    return prime

N = int(input())
# N 을 0으로 줄수도 있다 ㅡㅡ 문제 잘 읽자!
if N > 0:
    NUMS = list(map(int, input().split()))
    NUMS.sort()
    max_num = NUMS[N-1]

    # 1부터 ~ max_num 까지의 소수를 우선 다 구한다.
    primes = find_prime(max_num)
    count = 0
    for i in range(0, len(NUMS)):
        if NUMS[i] in primes:
            count += 1
else:
    count = 0
print(count)
