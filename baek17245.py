import sys
sys.stdin = open("baek17245.txt")


N = int(sys.stdin.readline().rstrip())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, sys.stdin.readline().split()))


total = 0
for r in range(0, N):
    for c in range(0, N):
        total += MAP[r][c]

target = total//2
if total%2:
    target += 1

left = 0
# 모든칸에 1천만개씩있을때 => 1천만/2만큼 시간이 필요
right = 10000001

while left < right:
    mid = (left+right)//2

    cur_sum = 0
    for r in range(0, N):
        for c in range(0, N):
            cur_sum += min(MAP[r][c], mid)
    # 시간이 충분 더 줄여본다
    if cur_sum >= target:
        right = mid
    else:
        left = mid+1
print(left)