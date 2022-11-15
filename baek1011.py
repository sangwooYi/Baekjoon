import sys
import math
sys.stdin = open("baek1011.txt")

"""
아이디어 1
현재 term이 n**2값보다 작아지기 직전의 n 을 구함
그 후에 아래 조건대로 분기해서 답을 출력!
    if term <= n**2:
        answer = 2*n-1
    elif term <= n**2+n:
        answer = 2*n
    else:
        answer = 2*n+1
"""

upper = math.ceil((2**31)**(1/2))
T = int(input())
for tc in range(0, T):
    x, y = map(int, input().split())
    term = y-x

    n = 1
    while n <= upper:
        if term < (n+1)**2:
            break
        n += 1
    
    if term <= n**2:
        answer = 2*n-1
    elif term <= n**2+n:
        answer = 2*n
    else:
        answer = 2*n+1
    print(answer)