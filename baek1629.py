import sys
sys.stdin = open("baek1629.txt")

"""
나머지 관련 공식
나머지 연산은 아래와같은 공식을 갖는다.
* + - 셋다 아래와같이 나머지 연산이 가능함!
즉 두 자연수 곱에 대한 나머지는, 그 각각의 나머지의 곱의 나머지와 같다
더하기, 빼기도 동일! 
+ , - , * 셋다 특정 두 수의 연산에 대한 나머지 값은, 각각의 수에 대한 나머지를 연산한 값의 나머지와 동일하다!
=> 이를 이용하여 분할 정복이 가능하단 의미!!! 이게 가장 point!

(A*B) % M = (A % M) * (B % M) % M
(A + B) % M = ((A % M) - (B % M)) % M

이 나머지 연산을 이용하는 문제

이문제 이해해보자.
재귀에 대한 이해도를 높여야 함

tip. 동일한 재귀를 여러번 사용해야할때는, 그 return 값을 저장해서
그걸 이용하자!
아래처럼 쓸때랑, 그때마다 재귀를 쓸때는 메모리 스택 효율에서 압도적인 차이가 난다!
(메모이제이션 효과랑 유사하게 생각하면 된다!)

따라서 
1. 나머지 연산에 대한 개념
2. 분할 정복 진행시 동일한 재귀함수를 사용하는 경우 tip
위의 두가지 아이디어가 포인트였던 문제!
"""

# 그냥 나는 아래와 같이 재귀임을 알수 있도록 코드를 짜자
def calc_mod(a, b, c):
    # 종료 조건
    if b == 1:
        return a % c

    # 단순히 동일한 재귀 상황에 대한 반복이 필요할때는 아래와 같이 return값을 받아서 그걸 사용할것!
    # 재귀가 진행되는 모양새는 똑같으나 아래와같이 return값을 받아서 쓴다면, 저장된 값만 전달되지만,
    # 기존에 하던대로 같은 재귀 함수를 계속 쓰면, 그 재귀함수 각각이 전부 진행되므로 효율에서 압도적인 차이가 난다.
    temp = calc_mod(a, b//2, c)

    if b % 2 == 0:
        return (temp * temp) % c
    
    else:
        return (temp * temp * a) % c


A, B, C = map(int, input().split())

ans = calc_mod(A, B, C)
print(ans)