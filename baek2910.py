import sys
sys.stdin = open("baek2910.txt")


N, C = map(int, input().split())
nums = list(map(int, input().split()))

check_dict = {}
for i in range(0, len(nums)):
    num = nums[i]
    if num in check_dict.keys():
        check_dict[num][1] += 1
    else:
        check_dict[num] = [i, 1]

answer_list = []
for key in check_dict:
    answer_list.append((check_dict[key][0], check_dict[key][1], key))

answer_list.sort(key=lambda x : (-x[1], x[0]))

for i in range(0, len(answer_list)):
    cnt = answer_list[i][1]
    num = answer_list[i][2]
    for j in range(0, cnt):
        if i == len(answer_list)-1 and j == cnt-1:
            print(num)
        else:
            print(num, end=" ")