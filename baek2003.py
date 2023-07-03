import sys
sys.stdin = open("baek2003.txt")



N, M = map(int, input().split())
nums = list(map(int, input().split()))

sum_arr = [0] * N
for i in range(0, N):
    if i == 0:
        sum_arr[i] = nums[i]
    else:
        sum_arr[i] = sum_arr[i-1]+nums[i]


cnt = 0
for i in range(0, N):
    # 0 ~ i 까지
    for j in range(0, i+1):
        cur_sum = sum_arr[i]
        if j > 0:
            cur_sum -= sum_arr[j-1]
        # 모드 양수이므로 (자연수) M 보다 작아지면 종료
        if cur_sum < M:
            break
        if cur_sum == M:
            cnt += 1
print(cnt)
