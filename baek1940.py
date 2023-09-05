import sys
sys.stdin = open("baek1940.txt")


N = int(input())
M = int(input())
materials = list(map(int, input().split()))
materials.sort()

visited = [False] * N

cnt = 0
pl = 0
pr = N-1

while pl < pr:
    cur = materials[pl] + materials[pr]

    if cur < M:
        pl += 1
    elif cur > M:
        pr -= 1
    else:
        pl += 1
        cnt += 1
print(cnt)