def find_prime(b):
    # 우선 b까지 모든 소수 체크

    for i in range(5, b+1, 2):
        flag = True
        for j in range(0, len(primes)):
            if primes[j]**2 > i:
                break
            if i % primes[j] == 0:
                flag = False
                break
        if flag:
            primes.append(i)

    

M = int(input())
N = int(input())

primes = [2, 3]
find_prime(N)

min_val = 9876543
total = 0
for num in range(M, N+1):
    if num in primes:
        min_val = min(min_val, num)
        total += num
if total == 0:
    print(-1)
else:
    print(total)
    print(min_val)