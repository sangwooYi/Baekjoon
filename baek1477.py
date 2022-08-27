import sys
sys.stdin = open("baek1477.txt")

N, M, L = map(int, input().split())
positions = list(map(int, input().split()))
positions = [0] + positions + [L]

positions.sort()

pl = 1
pr = L-1
answer = 0
while pl <= pr:
    count = 0
    mid = (pl+pr) // 2
    for i in range(1, len(positions)):
        term = positions[i] - positions[i-1]
        if term > mid:
            # 이런걸 혼자서 생각할 수 있어야 한다.
            count += ((term-1) // mid)
        
    if count > M:
        pl = mid+1
    else:
        pr = mid-1
        answer = mid
print(answer)
