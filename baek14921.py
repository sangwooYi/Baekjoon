import sys
sys.stdin = open("baek14921.txt")

N = int(sys.stdin.readline())
# 오름차순으로 주어짐
nums = list(map(int, sys.stdin.readline().split()))

pl = 0
pr = N-1


answer = 900000000
while pl < pr:
    now = nums[pl] + nums[pr]
    if now == 0:
        answer = 0
        break

    if abs(answer) > abs(now):
        answer = now
    if now > 0:
        pr -= 1
    else:
        pl += 1
print(answer)