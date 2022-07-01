import sys
sys.stdin = open("baek17387.txt")

"""
CCW 알고리즘! (Counter Clock Wise 알고리즘)

(x1, y1), (x2, y2),  (x3, y3) 에 대해서
임의의 세점에 대해서 방향성을 체크하는것
(x2-x1) * (y3-y1) - (y2-y1) * (x3-x1) 
> 0 이면 1 반시계
< 0 이면 -1 시계
= 0 이면 0 을 반환 평행하다는것

따라서 
A, B / C, D 에대해서
1                                       2
CCW(A, B, C) * CCW(A, B, D) <= 0 && CCW(C, D, A) * CCW(C, D, B) <= 0 일때,
만약 1, 2 둘다 0이라면

한번 반드시 반복하자!
"""

def ccw(x1, y1, x2, y2, x3, y3):
    # 신발끈 공식  
    #  x1 x2 x3    (x1y2+x2y3+x3y1) - (x2y1+x3y2+x1y3) 이다 (신발끈 공식)
    #  y1 y2 y3 
    # x2y3-x1y3-x2y1 - (y2x3-y1x3-x1y2) 인것 이걸 +x1y1 -xy1y을 해주면 아래처럼 인수분해가 되는것!
    tmp = (x2-x1) * (y3-y1) - (y2 - y1) * (x3 - x1) # 이 꼴을 기억해 두자
    if tmp > 0:
        return 1 # 반시계
    elif tmp < 0:
        return -1 # 시계
    else:
        return 0  # 평행


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4 ,y4 = map(int, input().split())
answer = 0
# 작은쪽이 다른 선분 큰쪽 이하여야 한다.
if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) == 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) == 0:
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
        answer = 1
elif ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) <= 0 and ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) <= 0:
    answer = 1

print(answer)