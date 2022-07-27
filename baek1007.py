import sys
import math
sys.stdin = open("baek1007.txt")

"""
v1 = (x2-x1, y2-y1)
v2 = (x4-x3, y4-y3) 일때
벡터의 합은
v1+v2 = ((x4+x2) - (x3+x1), (y4+y2) - (y3+y1)) 이다
이처럼 벡터 매칭의 합은 아래와 같다
v1+v2 .. vn = ((x 절반의 합) - (나머지 x의합), (y절반의 합) - (나머지 y의 합))
따라서 경우의수는 nCn//2 가 되며, 이 전체 경우중
최소의 값을 찾으면 된다.
"""

def comb(arr, start, visited, n, r):
    global x_total
    global y_total
    global min_vect_sum

    if r == 0:
        x1_sum = 0
        y1_sum = 0
        for i in range(0, len(arr)):
            if visited[i]:
                x1, y1 = arr[i]
                x1_sum += x1
                y1_sum += y1
        x2_sum = x_total - x1_sum
        y2_sum = y_total - y1_sum

        tmp_vect_sum = math.sqrt((x2_sum-x1_sum)**2 + (y2_sum-y1_sum)**2)
        min_vect_sum = min(min_vect_sum, tmp_vect_sum)
        return

    for i in range(start, len(arr)):
        if visited[i]:
            continue
        visited[i] = True
        comb(arr, i+1, visited, n, r-1)
        visited[i] = False
    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    coords = [0] * N
    x_total = 0
    y_total = 0
    min_vect_sum = 987654321

    for i in range(0, N):
        x, y = map(int, input().split())
        coords[i] = [x, y]
        x_total += x
        y_total += y
    check = [False] * N
    
    comb(coords, 0, check, N, N//2)
    print(min_vect_sum)