import sys
sys.stdin = open("baek1003.txt")

"""
0 1 1 2 3 5 8 13 21 34 55 .......
메모이제이션 사용 (재귀가 아니라 DP개념이다!!)
이 코드 아예 기억하자

그리고 직접해보면 이 문제는 fibo(n-1), fibo(n) 을 찾는 문제 (직접 바텀 업 해보면 알 수 있다!)
"""

def fibo(n):
    DP = [0, 1]
    if n < 2:
        return DP[n]
    # 메모이제이션 기억
    for i in range(2, n+1):
        DP.append(DP[i-1] + DP[i-2])
    return DP[n]


T = int(input())
# n은 0, 1 일때를 미리 처리 그리고 전역 리스트로 선언해서 계속 누적되게 만든다.
NUMS = [0] * T
for i in range(0, T):
    NUMS[i] = int(input())

for i in range(0, T):
    now = NUMS[i]
    answer1 = fibo(now-1)
    answer2 = fibo(now)   
    print(answer1, answer2)