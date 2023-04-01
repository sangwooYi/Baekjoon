import sys
import math
sys.stdin = open("baek1011.txt")

"""
1+2+1 = 2**2
1+2+3+2+1 = 3**2
이런식임!!

아이디어 1
현재 term이 n**2값보다 작아지기 직전의 n 을 구함
그 후에 아래 조건대로 분기해서 답을 출력!
    if term <= n**2:
        answer = 2*n-1
    elif term <= n**2+n:
        answer = 2*n
    else:
        answer = 2*n+1

# 1669번 풀이가 진짜 풀이다.. 나중에 참조할것!
내 풀이는 1669번 풀이에 결과론적 풀이일뿐임
( 이거 내가 혼자 발견한것도 대견하네..;;)
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