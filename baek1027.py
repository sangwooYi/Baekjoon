import sys
sys.stdin = open("baek1027.txt")

"""
그냥 N이 50이므로 브루트 포스

두 점이 주어질때 선분
(a1, b1), (a2, b2)   (a1 != a2)
y = (b1-b2)/(a2-a1)*(x-a1) + b1

이때 그 사이의 점이 (a3, b3) 일때

(b1-b2)/(a2-a1)*(a3-a1)+b1 이 M 일때

a1 a2 사이의 모든 점이 M > b3 를 만족해야 서로 보인다!

"""


def check_height(m1, m2, m3):
    x1, y1 = m1
    x2, y2 = m2
    x3, y3 = m3

    line_between = ((y1-y2)/(x1-x2))*(x3-x1)+y1
    if line_between > y3:
        return True
    return False


N = int(input())
height = list(map(int, input().split()))

max_cnt = 0
for i in range(0, N):
    tmp = 0
    start = (i, height[i])
    for j in range(i-1, -1, -1):
        end = (j, height[j])
        flag = True
        for k in range(j+1, i):
            mid = (k, height[k])
            if not check_height(start, end, mid):
                flag = False
                break
        if flag:
            tmp += 1
    for j in range(i+1, N):
        end = (j, height[j])
        flag = True
        for k in range(i+1, j):
            mid = (k, height[k])
            if not check_height(start, end, mid):
                flag = False
                break
        if flag:
            tmp += 1
    max_cnt = max(max_cnt, tmp)
answer = max_cnt
print(answer)