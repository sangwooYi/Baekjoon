import sys
from collections import deque
sys.stdin = open("baek17394.txt")



primes = [2, 3]
prime_dict = {2: 1, 3: 1}

for i in range(5, 100001, 2):
    flag = False

    for j in range(0, len(primes)):
        if primes[j]**2 > i:
            break
        if i % primes[j] == 0:
            flag = True
            break
    # 안나누어떨어져야함
    if not flag:
        primes.append(i)
        prime_dict[i] = 1

def find_min(num, lower, upper):
    # 문제좀 잘 읽자..
    if lower <= num <= upper:
        if num in prime_dict:
            return 0
    
    visited = [False] * 1000001
    que = deque()

    visited[num] = True
    que.append((num, 0))

    while que:
        now, cnt = que.popleft()

        for i in range(0, 4):
            if i == 0:
                next_num = now//2
            elif i == 1:
                next_num = now//3
            elif i == 2:
                next_num = now+1
            elif i == 3:
                next_num = now-1
            if next_num > 1000000 or next_num < 0:
                continue
            if visited[next_num]:
                continue    
            visited[next_num] = True
            if lower <= next_num <= upper:
                if next_num in prime_dict:
                    return cnt+1
            que.append((next_num, cnt+1))
    return -1

T = int(input())
for tc in range(0, T):
    N, A, B = map(int, input().split())
    answer = find_min(N, A, B)
    print(answer)