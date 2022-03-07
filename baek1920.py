import sys
sys.stdin = open("baek1920.txt")

"""
전형적인 이분탐색!
"""


def is_it_has_or_not(arr, num):
    pl = 0
    pr = len(arr) - 1

    while pl <= pr:
        pc = (pl + pr) // 2
        # 존재하면 1 출력
        if arr[pc] == num:
            return 1
        elif arr[pc] > num:
            pr = pc - 1
        else:
            pl = pc + 1
    # 없으면 0 출력
    return 0

N = int(input())
AN = list(map(int, input().split()))
AN.sort()
M = int(input())
NUMBERS = list(map(int, input().split()))
answer = []
for i in range(0, M):
    now = is_it_has_or_not(AN, NUMBERS[i])
    answer.append(now)
for i in range(0, len(answer)):
    print(answer[i])