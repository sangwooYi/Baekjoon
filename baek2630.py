import sys
sys.stdin = open("baek2630.txt")
"""
파란색이 1 하얀색이 0
"""


def origami(pu, pd, pl, pr, arr):
    global white
    global blue

    # 종료조건1 길이가 1일때
    if pu == pd and pl == pr:
        if arr[pu][pl] == 1:
            blue += 1
        elif arr[pu][pl] == 0:
            white += 1
        return
    # 종료조건2 모두 같은 색일때
    flag = True
    start = arr[pu][pl]
    for row in range(pu, pd+1):
        if not flag:
            break
        for col in range(pl, pr+1):
            if arr[row][col] != start:
                flag = False
                break
    if flag:
        if start == 1:
            blue += 1
        elif start == 0:
            white += 1
        return

    term = (pr - pl + 1) // 2
    # 1사분면
    origami(pu, pu+term-1, pl, pl+term-1, arr)

    # 2사분면
    origami(pu, pu+term-1, pl+term, pr, arr)

    # 3사분면
    origami(pu+term, pd, pl, pl+term-1, arr)

    # 4사분면
    origami(pu+term, pd, pl+term, pr, arr)



N = int(input())
MAP = [0] * N
for i in range(0, N):
    temp = list(map(int, input().split()))
    MAP[i] = temp
white = 0
blue = 0
origami(0, N-1, 0, N-1, MAP)
print(white)
print(blue)