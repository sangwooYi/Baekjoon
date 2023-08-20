import sys
sys.stdin = open("baek1713.txt")


N = int(input())
T = int(input())
nums = list(map(int, input().split()))

arr = []


for i in range(0, len(nums)):
    num = nums[i]
    if arr:
        # 현재 후보에 있으면 그냥 횟수만 추가
        flag = False
        for j in range(0, len(arr)):
            if arr[j][0] == num:
                arr[j][1] += 1
                flag = True
                break
        if not flag:
            if len(arr) >= N:
                # 투표횟수 내림차순, 인덱스 내림차순
                arr.sort(key=lambda x : [-x[1], -x[2]])
                arr.pop()
            arr.append([num, 1, i])
    # 비어있으면 일단 추가
    else:
        arr.append([num, 1, i])
arr.sort()
for i in range(0, len(arr)):
    if i < len(arr)-1:
        print(arr[i][0], end=" ")
    else:
        print(arr[i][0])
