import sys
sys.stdin = open("baek2352.txt")


N = int(input())
nums = list(map(int, input().split()))

LIS = [nums[0]]

for i in range(1, N):
    num = nums[i]

    # LIS 마지막값보다 그냥 큰값이면 추가
    if LIS[-1] < num:
        LIS.append(num)
    # LIS 마지막 값 이하라면, lower bound 진행
    else:
        left = 0
        right = len(LIS)
        
        # LIS에서 들어갈 수 있는 가장 낮은 위치를 찾는것
        while left < right:
            mid = (left+right)//2

            # 탐색범위를 줄인다. 현재 탐색위치의 값이 num 보다 크거나 같으면 LIS에서 더 낮은위치로 이동
            if LIS[mid] >= num:
                right = mid
            # LIS 현재 탐색값이 num 보다 작다면 탐색범위를 키운다. 더 큰 위치에 있어야 하는것
            else:
                left = mid+1
        LIS[left] = num
print(len(LIS))