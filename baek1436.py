import sys
sys.stdin = open("baek1436.txt")

"""
그냥 
"""

def find_num(n):
    num = 666
    order = 1
    while True:
        if order == n:
            return num
        num += 1
        temp = str(num)
        # 문자열에서 특정 문자열 포함관계 문제 풀때 그냥 이렇게 하자!
        if "666" in temp:
            order += 1


N = int(input())
answer = find_num(N)
print(answer)