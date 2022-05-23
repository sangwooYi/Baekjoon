import sys
sys.stdin = open("baek13172.txt")

"""
(a+b)modN = (amodN + bmodN)modN
(a-b)modN = (amodN - bmodN)modN
(a*b)modN = (amodN * bmodN)modN

모듈러 역원 b-1 은 modN에서 b * b-1 의 나머지가 1 이 되게하는 값 
즉 b = 3이고 모듈러 X 가 11일때, b-1은 4  (3*4 는 12이므로 1mod11 임)

Q = Si/Ni 

이때 문제에서 b**(-1)modX = b**(X-2)
즉 (Si*Ni^-1)modX == (SimodX * Ni**-1modX)modX == (SimodX * b**X-2)modX
이걸 쭉 합하면 됨!

(a*a*a*a)modx = (amodx * amodx * amodx * amodx)modx 
분할정복할때 이부분을 요긴하게 쓰자!

기본적으로 거듭제곱은 아래 로직
근데 파이썬도 너무 큰수는 출력을 못한다!
def pow(a, n):
    if n == 0:
        return 1
    temp = pow(a, n//2)
    if n %  2 == 0:
        return temp * temp
    else:
        return temp * temp * a
"""
 
# 거듭 제곱 a**n 요 알고리즘 꼭 챙겨두자 복잡도는 O(logN)
# b**(x-2)modx = (bmodx * bmodx ....)modx 이므로 아래처럼 해결 해야 한다.
# 파이썬도 너무 큰 수는 출력을 못함
def power(a, m):
    global x
    # 종료 조건
    if m == 0:
        return 1
    # 어차피 5//2 == 2 이므로 (내림) n%2 == 1 (홀수) 일때 그냥 n//2 해도 우리가 원하는 값이 나온다 
    # temp를 통해 중복되는 연산을 싹 쳐낸것
    temp = power(a, m//2)
    if m % 2 == 0:
        return (temp * temp) % x
    else:
        return (temp * temp * a) % x


M = int(input())
answer = 0
x = 1000000007
for i in range(0, M):
    # N, S
    n, s = map(int, input().split())
    n_inv = power(n, x-2)
    answer += (n_inv*s)%x
    answer = answer % x
print(answer)