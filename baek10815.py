import sys
sys.stdin = open("baek10815.txt")



def binary_search(arr, num):
    min = 0
    max = len(arr) - 1

    while min <= max:
        mid = (min + max) // 2

        if num == arr[mid]:
            return 1
        elif num < arr[mid]:
            max = mid-1
        else:
            min = mid+1
    return 0

def find_had_it(mine, finds):
    result = [0] * len(finds)

    for i in range(0, len(finds)):
        result[i] = binary_search(mine, finds[i])
    return result


N = int(input())
NUMS_N = list(map(int, input().split()))
# 이분탐색은 정렬된 조건이 필수다
NUMS_N.sort()
M = int(input())
NUMS_M = list(map(int, input().split()))

answer = find_had_it(NUMS_N, NUMS_M)
for i in range(0, len(answer)):
    if i == len(answer) - 1:
        print(answer[i])
    else:
        print(answer[i], end=" ")
