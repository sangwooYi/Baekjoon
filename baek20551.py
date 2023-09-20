import sys
sys.stdin = open("baek20551.txt")

"""
기본적으로 lower bound를 해야함!
"""

def lower_bound(arr, num):


    pl = 0
    pr = len(arr)

    flag = False
    while pl < pr:
        pc = (pl+pr)//2

        cur = arr[pc]

        if cur < num:
            pl = pc+1
        else:
            if cur == num:
                flag = True
            pr = pc
    if flag:
        return pl
    else:
        return -1


N, M = map(int, sys.stdin.readline().split())
arr = [0] * N
for i in range(0, N):
    arr[i] = int(sys.stdin.readline().rstrip())

arr.sort()
for i in range(0, M):
    num = int(sys.stdin.readline().rstrip())

    print(lower_bound(arr, num))