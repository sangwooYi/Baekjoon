import sys
sys.stdin = open("baek6439.txt")

"""
직사각형 네 모서리 좌표
(xl, yb)
(xl, yt)
(xr, yb)
(xr, yt)

따라서 여기서 나오는 네 선분은
(xl, yb) - (xl, yt)
(xr, yb) - (xr, yt)
(xl, yt) - (xr ,yt)
(xl, yb) - (xr, yb)

선분이 직사각형과 교차하는지 (혹은 포함되는지) 구하는 법
1. 포함관계 조사
xl <= min(xs, xe) and max(xs, xe) <= xr and max(ys, ye) <= yt and min(ys, ye) >= yb 면 True

2. 교차관계 조사
ccw 이용, 직사각형 네선분과 모두 체크하여 하나라도 교차하는게 나오면 True

교차 or 포함 관계 나오면 True
"""

def ccw(x1, y1, x2, y2, x3, y3):

    check = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)
    # 반시계
    if check > 0:
        return 1
    # 시계
    elif check < 0:
        return -1
    # 포함
    else:
        return 0


def is_cross(line, xs, ys, xe, ye):
    
    x1, y1 = line[0]
    x2, y2 = line[1]
 
    answer = False
    # 평행한 부분이 있을 때
    if ccw(x1, y1, x2, y2, xs, ys)*ccw(x1, y1, x2, y2, xe, ye) == 0 and ccw(xs, ys, xe, ye, x1, y1)*ccw(xs, ys, xe, ye, x2, y2) == 0:
        # x, y 모두 서로의 최솟값이 반대의 최댓값보다 이하에 있어야 평행한경우에도 만나는 부분이 생김
        if min(x1, x2) <= max(xs, xe) and min(xs, xe) <= max(x1, x2) and min(y1, y2) <= max(ys, ye) and min(ys, ye) <= max(y1, y2):
            answer = True
    elif ccw(x1, y1, x2, y2, xs, ys)*ccw(x1, y1, x2, y2, xe, ye) <= 0 and ccw(xs, ys, xe, ye, x1, y1)*ccw(xs, ys, xe, ye, x2, y2) <= 0:
        answer = True
    return answer

T = int(input())
for _ in range(0, T):
    flag = False

    xs, ys, xe, ye, x1, y1, x2, y2 = map(int, input().split())

    # 가공이 필요
    xl = min(x1, x2)
    xr = max(x1, x2)
    yb = min(y1, y2)
    yt = max(y1, y2)

    line1 = [[xl, yb], [xl, yt]]
    line2 = [[xr, yb], [xr, yt]]
    line3 = [[xl, yt], [xr, yt]]
    line4 = [[xl, yb], [xr, yb]]

    # 포함관계 조사
    if xl <= min(xs, xe) and xr >= max(xs, xe) and yt >= max(ys, ye) and yb <= min(ys, ye):
        flag = True

    if is_cross(line1, xs, ys, xe, ye) or is_cross(line2, xs, ys, xe, ye) or is_cross(line3, xs, ys, xe, ye) or is_cross(line4, xs, ys, xe, ye):
        flag = True
    if flag:
        print("T")
    else:
        print("F")
