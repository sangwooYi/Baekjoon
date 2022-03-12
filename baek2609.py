import sys
from tempfile import tempdir
sys.stdin = open("baek2609.txt")

"""
최대공약수 gcd (Gratest Common Divisor)
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

최소공배수 lcm (Least Common Multiple)
최대 공약수가 A라면
a = AC
b = AD  
lcm = ACD == (a * b) // gcd
"""

def gcd(a, b):
    while b > 0:
        temp = a
        a = b
        b = temp % b
    return a

def lcm(a, b):
    gc = gcd(a, b)  
    lc = a * b // gc
    return lc


N, M = map(int, input().split())

a_gcd = gcd(N, M)
a_lcm = lcm(N, M)
print(a_gcd)
print(a_lcm)
