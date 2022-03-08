import sys
sys.stdin = open("baek4153.txt")

"""
이건 입력받는 연습!
"""

while True:
    arr = list(map(int, input().split()))
    if arr == [0, 0, 0]:
        break
    arr.sort()
    
    c_pow = arr[2] ** 2
    b_pow = arr[1] ** 2
    a_pow = arr[0] ** 2
    if c_pow == (a_pow + b_pow):
        print("right")
    else:
        print("wrong")