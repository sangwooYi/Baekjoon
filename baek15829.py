import sys
sys.stdin = open("hashing.txt")

"""
ord(A) = 65
ord(a) = 97 인것만 잊지말자!
"""

def calc_hash(chars):
    result = 0
    for i in range(0, len(chars)):
        num = ord(chars[i]) - 96
        result += num * (31 ** i)
    return result

M = 1234567891
L = int(input())
in_list = list(input())

answer = calc_hash(in_list)
# M 과의 나머지연산값을 구하는거다! 따라서 M값보다 커질때는 나머지 값이 나와줘야함
print(answer % M)