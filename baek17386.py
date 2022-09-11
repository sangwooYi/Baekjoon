import sys
sys.stdin = open("baek17386.txt")

"""
CCW (CounterClockWise) 
말그대로 반시계 판별 법

구두끈 공식을 사용하며.

(x1*y2 + y2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)

이 값이 > 0 이면 반시계, < 0 이면 시계, == 0 이면 평행 임
 
부호는 선분이 다른 세번째 점에 비해 큰 쪽에 있는지, 작은쪽에 있는지 판별
 1 
  
3    2   (이래서 > 0 인것)


1

   2    3  (이래서 < 0 인것)

1 2 3   (이래서 == 0 인것)
"""

def ccw(x1, y1, x2, y2, x3, y3):

    # 구두끈 공식
    check = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)

    # 반시계 방향   
    if check > 0:
        return 1
    # 시계 방향
    elif check < 0:
        return -1
    # 평행
    else:
        return 0

L1 = list(map(int, input().split()))
L2 = list(map(int, input().split()))

x1, y1, x2, y2 = L1
x3, y3, x4, y4 = L2


answer = 0
if ccw(x1, y1, x2, y2, x3, y3)*ccw(x1, y1, x2, y2, x4, y4) == 0 and ccw(x3, y3, x4, y4, x1, y1)*ccw(x3, y3, x4, y4, x2, y2) == 0:
    # 평행일 때는, 서로의 최솟값이 서로의 최댓값보다 작은쪽에 있어야 한다. (그래야 만나는 영역이 생김)
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
        answer = 1
elif ccw(x1, y1, x2, y2, x3, y3)*ccw(x1, y1, x2, y2, x4, y4) <= 0 and ccw(x3, y3, x4, y4, x1, y1)*ccw(x3, y3, x4, y4, x2, y2) <= 0:
    answer = 1
print(answer)

