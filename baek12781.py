import sys
sys.stdin = open("baek12781.txt")


def ccw(x1, y1, x2, y2, x3, y3):

    check = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)
    if check > 0:
        return 1
    elif check < 0:
        return -1
    else:
        return 0


x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

answer = 0
# 완벽하게 교차해야만 한다.
if ccw(x1, y1, x2, y2, x3, y3)*ccw(x1, y1, x2, y2, x4, y4) < 0 and ccw(x3, y3, x4, y4, x1, y1)*ccw(x3, y3, x4, y4, x2, y2) < 0:
    answer = 1
print(answer) 