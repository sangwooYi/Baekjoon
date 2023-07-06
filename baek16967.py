import sys
sys.stdin = open("baek16967.txt")


"""
row 가 H / col이 W인 배열을
세로로 X만큼 가로로는 Y만큼 이동

그냥 본인 요소만 갖는 부분
영역1.
col 0 ~ Y-1  ( Y >= 1) 
일때 row를 0 ~ H-1

row 0 ~ X-1 ( X >= 1)
일떄 col을 0 ~ W-1

영역2 
col W-Y ~ W-1 까지 ( Y >= 1) 
=> 전체 좌표에서는 W ~ W+Y-1
일때 row 0 ~ H-1 
=> 전체 좌표 X ~ H+X-1 

row H-X ~ H-1 까지 ( X >= 1)
=> 전체 좌표에서는 H ~ H+X-1
일때 col 0 ~ W-1
=> 전체 좌표 Y ~ W+X-1 

영역3, 겹치는 부분
row는 X ~ H-X-1 까지 2X 만큼
col은 Y ~ W-Y-1까지 2Y만큼

그냥 가장 좌측에서부터 우대각선 방향으로 차례차례 찾아가면 끝
현재 찾으려는값 xi, yi일때 그 값은 
현재 위치 값 - (xi-X, yi-Y) 값을 빼면 됨
"""


H, W, X, Y = map(int, input().split())
full_map = [0] * (H+X)

for i in range(0, (H+X)):
    full_map[i] = list(map(int, input().split()))
 
org_arr = [[0] * W for _ in range(0, H)]

# 영역 1
for c in range(0, Y):
    for r in range(0, H):
        org_arr[r][c] = full_map[r][c]
for r in range(0, X):
    for c in range(0, W):
        org_arr[r][c] = full_map[r][c]

# 영역 2
for c in range(W, W+Y):
    for r in range(X, H+X):
        org_arr[r-X][c-Y] = full_map[r][c]
for r in range(H, H+X):
    for c in range(Y, W+Y):
        org_arr[r-X][c-Y] = full_map[r][c]

# 영역 3
for r in range(X, H-X):
    for c in range(Y, W-Y):
        org_arr[r][c] = full_map[r][c]-org_arr[r-X][c-Y]

for r in range(0, H):
    print(" ".join(map(str, org_arr[r])))