import sys
sys.stdin = open("baek13172.txt")

"""
(a+b)modN = (amodN + bmodN)modN
(a-b)modN = (amodN - bmodN)modN
(a*b)modN = (amodN * bmodN)modN

모듈러 역원 b-1 은 modN에서 b * b-1 의 나머지가 1 이 되게하는 값 
즉 b = 3이고 모듈러 X 가 11일때, b-1은 4  (3*4 는 12이므로 1mod11 임)

Q = Si/Ni 
이때 Ni*(-1) = (mod+1)//Ni 
따라서 (((mod+1)//Ni)*Si) % mod 가 우리가 원하는 답 

이거 나중에 풀자 ㅠㅠ
"""


M = int(input())
arr = [0] * M
for i in range(0, M):
    arr[i] = list(map(int, input().split()))

mod = 1000000007
a = 3
# 이게 역원
a_m1 = (mod+1) // a
print((a_m1*7)%mod)
