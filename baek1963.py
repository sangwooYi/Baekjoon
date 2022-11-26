import sys
from collections import deque
sys.stdin = open("baek1963.txt")



primes = [2, 3]
primes_dict = {2: 1, 3: 1}
# 소수 판정 잘 익혀두자!
for i in range(5, 100000, 2):
    flag = True
    for prime in primes:
        if prime**2 > i:
            break
        if i%prime==0:
            flag = False
            break
    if flag:
        primes.append(i)
        primes_dict[i] = 1


def find_min(num1, num2):

    # 같은 경우는 그냥 예외로 처리
    if num1 == num2:
        return 0

    chek_dict = {}
    chek_dict[num1] = 1

    que = deque()
    que.append((num1, 0))


    while que:
        now_num, cnt = que.popleft()
        for idx in range(0, 4):
            for digit in range(0, 10):
                if idx == 0 and digit == 0:
                    continue
                if int(now_num[idx]) == digit:
                    continue
                tmp = ''
                for i in range(0, 4):
                    if i == idx:
                        tmp += str(digit)
                    else:
                        tmp += now_num[i]

                if tmp == num2:
                    return cnt+1

                conv_to_num = int(tmp)
                
                if conv_to_num not in primes_dict.keys():
                    continue
                if tmp in chek_dict.keys():
                    continue
                chek_dict[tmp] = 1
                que.append((tmp, cnt+1))
        
    return "Impossible"

T = int(input())
for t in range(0, T):
    num1, num2 = input().split()


    answer = find_min(num1, num2)
    print(answer)