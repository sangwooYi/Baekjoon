import sys
sys.stdin = open("baek15666.txt")

"""
순열, 비내림차순순열, 조합 전부 작성할 수 있어야한다.
"""


def baek15666(arr, out, depth, start, n, r):
    if depth == r:
        if tuple(out) not in check_dict.keys():
            check_dict[tuple(out)] = 1
            for i in range(0, len(out)):
                if i == len(out)-1:
                    print(out[i])
                else:
                    print(out[i], end=" ")
        return
    for i in range(start, len(arr)):
        out[depth] = arr[i]
        baek15666(arr, out, depth+1, i, n, r)

N, M = map(int, input().split())
nums = list(map(int, input().split()))
temp = [0] * M
check_dict = {}
nums.sort()
baek15666(nums, temp, 0, 0, N, M)