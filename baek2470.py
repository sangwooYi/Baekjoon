import sys
sys.stdin = open("baek2470.txt")


N = int(sys.stdin.readline())
solutions = list(map(int, sys.stdin.readline().split()))
solutions.sort()

INF = 987654321


pl = 0
pr = N-1

ans_left = pl
ans_right = pr

closest = abs(solutions[ans_left] + solutions[ans_right])

while pl < pr:
    now = solutions[pl] + solutions[pr]
    # 끝
    if now == 0:
        ans_left = pl
        ans_right = pr
        break
    if abs(now) < closest:
        ans_left = pl
        ans_right = pr
        closest = abs(now)
    if now < 0:
        pl += 1
    elif now > 0:
        pr -= 1
print(solutions[ans_left], solutions[ans_right])