import sys

# lower bound
def binary_search_left(key):

    left = 0
    right = len(LIS)

    while left < right:
        mid = (left+right)//2

        # 범위를 더 줄여본다
        if LIS[mid] >= key:
            right = mid
        else:
            left = mid+1
    return left
        

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

LIS = [nums[0]]

for i in range(1, N):
    num = nums[i]
    if LIS[-1] < num:
        LIS.append(num)
    else:
        idx = binary_search_left(num)
        LIS[idx] = num
print(N-len(LIS))
