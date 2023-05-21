N = int(input())
nums = list(map(int, input().split()))


max_ans = 0
flag = True
for i in range(0, N-1):
    if flag:
        first_num = nums[i]
        flag = False
    # 오르막길 유지
    if nums[i] < nums[i+1]:
        if i == N-2:
            cur_res = nums[i+1]-first_num
            max_ans = max(max_ans, cur_res)
        continue
    # 오르막길 X
    cur_res = nums[i]-first_num
    max_ans = max(max_ans, cur_res)
    flag = True
print(max_ans)

