import sys
sys.stdin = open("baek2166.txt")

"""
신발끈 공식!
2차원 평면상에 N개의 좌표가 다음과 같이 있을때, 다각형의 면적을 구할 수 있다
x1 x2 x3 x4
y1 y2 y3 y4
이렇게 네개의 점이 있다면
이 점을 잇는 다각형의 면적은
1/2*((x1y2+x2y3+x3y4+x4y1)-(x2y1+x3y2+x4y3+x1y4)) 이렇게 구할 수 있고
이걸 신발끈 공식이라고 함!
"""

N = int(sys.stdin.readline())
coords = [0] * N
for i in range(0, N):
    coords[i] = list(map(int, sys.stdin.readline().split()))

front = 0
rear = 0

for i in range(0, N):
    tmp = (i+1) % N
    front += (coords[i][0]*coords[tmp][1])
    rear += (coords[tmp][0]*coords[i][1])



# 어차피 정수끼리 합차를 2로 나누는것이므로 어차피 소숫점 한자리임
area = (abs(front-rear))/2
print(area)