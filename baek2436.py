import sys
import math
sys.stdin = open("baek2436.txt")

"""
num1*num2//gcd = lcd 임

num1 = x*gcd
num2 = y*gcd

lcd = x*y*gcd 임
따라서 lcd // gcd 는
x * y
이때 x, y는 서로소여야 한다! 
=>a의 약수를 찾을때 루트 a까지만 탐색하는것을 이용!
"""

A, B = map(int, input().split())

# gcd 공약수 구하는 로직 잘 기억하자!
def is_coprime(a, b):

    larger = max(a, b)
    smaller = min(a, b)

    while (smaller != 0):
        r = larger % smaller
        larger = smaller
        smaller = r
    if larger == 1:
        return True
    return False


num = B//A
root_num = num**(1/2)
INF = 987654321987
min_sum = INF
num1 = 1
num2 = num
for i in range(1, math.ceil(root_num)):
    if num % i == 0:
        if is_coprime(i, num//i):
            tmp_sum = i + num//i
            if min_sum > tmp_sum:
                min_sum = tmp_sum
                num1 = i
                num2 = num//i
print(f"{num1*A} {num2*A}")