import sys
sys.stdin = open("baek1253.txt")

"""
문제를 잘 읽자

두 수의 합이 '다른' 수와 같아 질 때임
근데, 또 다른 위치면 다른수임
"""

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

num_dict = {}
for num in nums:
    if num in num_dict.keys():
        num_dict[num] += 1
    else:
        num_dict[num] = 1

check_dict = {}
answer = 0
if N > 1:
    for i in range(0, N-1):
        for j in range(i+1, N):
            tmp_sum = nums[i] + nums[j]
            # 0 으로 인해 반례들이 나온다! 이런거 생각할 수 있어야 함!!
            if nums[i] == 0 or nums[j] == 0:
                if tmp_sum:
                    if num_dict[tmp_sum] == 1:
                        continue
                else:
                    if num_dict[tmp_sum] <= 2:
                        continue
            if tmp_sum in num_dict.keys():
                if tmp_sum not in check_dict.keys():
                    check_dict[tmp_sum] = 1
                    answer += num_dict[tmp_sum]
print(answer)