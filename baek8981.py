import sys
sys.stdin = open("baek8981.txt")


N = int(input())
nums = list(map(int, input().split()))

answer_arr = [0] * N

cnt = 0
idx = 0
while cnt < N:
    while answer_arr[idx] != 0:
        idx = (idx+1)%N
    answer_arr[idx] = nums[cnt]
    idx = (nums[cnt]+idx)%N
    cnt += 1
print(N)
print(" ".join(map(str, answer_arr)))