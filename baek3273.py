N = int(input())
nums = list(map(int, input().split()))
X = int(input())
nums.sort()

pl = 0
pr = N-1

cnt = 0
while pl < pr:
    now = nums[pl] + nums[pr]

    if now > X:
        pr -= 1
    else:
        if now == X:
            cnt += 1
        pl += 1
print(cnt)
        