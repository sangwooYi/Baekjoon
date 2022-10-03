import sys
import bisect # lower_bound 는 bisect_left  // upper_bound 는 bisect_right로 쉽게 구현 가능 
sys.stdin = open("baek14003.txt")

"""
https://velog.io/@seho100/최강-증가-부분-수열LIS-알고리즘 참고

O(NlogN)
은 기본적으로 lower bound이용 
(참고 
lower bound는 해당 조건을 만족하는 범위중 가장 왼쪽 작은 위치를 찾는것, 즉 처음 조건을 만족하는 위치
upper bound는 처음으로 해당 조건 범위를 가장 먼저 벗어나는 위치를 찾는 것, 따라서 -1 위치가 가장 마지막으로 조건을 만족하는 위치)
arr[i] < arr[i+1] 벡터에 저장
arr[i] >= arr[i+1] 이면 arr[i+1]이 들어올 수 있는 자리를 찾아서 교환.
그리고 진행하면서 DP에, 현재 arr[i]이 실제 LIS에 들어올 위치를 저장 
ex)
1 4 3 2 6 8
이라면, 일단 LIS는 4이고,
실제 배열  1 4 3 2 6 8
DP =      1 2 2 2 3 4   이런식으로 DP에 저장되는것
이걸 역으로 탐색하며 실제배열에서 LIS갯수만 큼 뽑아낸 후,
오름차순 정렬하면 끝!
"""

# N = int(sys.stdin.readline())
# nums = [0] + list(map(int, sys.stdin.readline().split()))

# DP = [0] * (N+1)
# LIS = [-99876654321]

# for i in range(1, N+1):
#     num = nums[i]
#     if LIS[-1] < num:
#         LIS.append(num)
#         DP[i] = len(LIS)-1
#     else:       # lower bound
#         DP[i] = bisect.bisect_left(LIS, num)
#         LIS[DP[i]] = num
# lis_len = len(LIS)-1

# max_idx = max(DP)+1
# ans = []
# for i in range(N, 0, -1):
#     if DP[i] == max_idx-1:
#         ans.append(nums[i])
#         max_idx = DP[i]
# print(lis_len)
# ans.sort()
# print(" ".join(map(str, ans)))


# 그냥 내풀이가 더 직관적이다! (가능하면 기억 안나지않는한 직접 구현하자)
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

DP = [0] * N
LIS = [nums[0]]
DP[0] = 0
for i in range(1, N):
    num = nums[i]
    if LIS[-1] < num:
        LIS.append(num)
        # LIS에서 올 위치 저장이 목표!
        DP[i] = len(LIS)-1   # 여길 max(DP)+1로 해서 시간 초과...
    else:
        pl = 0
        pr = len(LIS)-1
        # lower bound는 이게 맞다!
        while pl < pr:
            pc = (pl+pr)//2
            # 다른조건은동일, lower bound는 조건 == arr[pc] 일지라도 우측 범위를 줄이고,
            # upper bound는 조건 == arr[pc] 일지라도 왼쪽 범위를 줄이는게 끝! (목표는 위에 주석 설명을 참고)
            # 그냥 값 자체를 찾는것은 조건 == arr[pc]인 순간 종료
            if LIS[pc] >= num:
                pr = pc
            else:
                pl = pc+1
        # 그냥 가장 끝범위에 와야하는 경우
        LIS[pl] = num
        DP[i] = pl

lis_len = len(LIS)

tmp = [0] * lis_len
r = lis_len-1
for i in range(N-1, -1, -1):
    if r < 0:
        break
    if DP[i] == r:
        tmp[r] = nums[i]
        r -= 1
tmp.sort()
print(lis_len)
print(" ".join(map(str, tmp)))