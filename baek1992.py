import sys
sys.stdin = open("baek1992.txt")


"""
이제 분할정복은 좀 익숙해진듯?
"""


def quadTree(pu, pd, pl, pr):
    global ans
    # 종료 조건
    if (pu == pd) or (pl == pr):
        ans += str(MAP[pu][pl])
        return
    flag = True
    start = MAP[pu][pl]
    for row in range(pu, pd+1):
        if not flag:
            break
        for col in range(pl, pr+1):
            if MAP[row][col] != start:
                flag = False
                break
    # 모두 같은 값! 종료조건
    if flag:
        ans += str(start)
        return
    term = (pr - pl + 1) // 2
    ans += "("
    # 1사분면
    quadTree(pu, pu+term-1, pl, pl+term-1)
    # 2사분면
    quadTree(pu, pu+term-1, pl+term, pr)
    # 3사분면
    quadTree(pu+term, pd, pl, pl+term-1)
    # 4사분면
    quadTree(pu+term, pd, pl+term, pr)
    ans += ")"


N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input()))
ans = ""
quadTree(0, N-1, 0, N-1)
print(ans)