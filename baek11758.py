import sys
sys.stdin = open("baek11758.txt")

"""
CCW 알고리즘

세 이차원 좌표가 주어질 때
(x2-x1) * (y3-y1) - (y2-y1) * (x3-x1) 
> 0 이면 1 반시계
< 0 이면 -1 시계
= 0 이면 0 평행

신발끈 공식에서부터 나왔으며,
(x1y2+x2y3+x3y1) - (x2y1+x3y2+x1y3) +x1y1 -x1y1
을 인수분해하면 위와 같이 되는 것!

따라서 안외워지면 그냥 
CCW 판단을 (x1y2+x2y3+x3y1) - (x2y1+x3y2+x1y3) 신발끈 공식으로 할 것!
"""

def ccw(p1, p2, p3):
    front = (p2[0]-p1[0]) * (p3[1]-p1[1])
    rear = (p2[1]-p1[1]) * (p3[0]-p1[0])
    
    point = front - rear
    
    if point > 0:
        result = 1
    elif point < 0 :
        result = -1
    else:
        result = 0
    return result


P1 = list(map(int, input().split()))
P2 = list(map(int, input().split()))
P3 = list(map(int, input().split()))

answer = ccw(P1, P2, P3)
print(answer)
