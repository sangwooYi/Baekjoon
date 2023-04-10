import sys
sys.stdin = open("baek16507.txt")

"""
우선 (0, 0) ~ (r, c) 까지의 합을 구한후

(r1, c1) ~ (r2, c2) 까지의 합은
→
(0, 0) ~ (r2, c2) 까지의 합 
- (0, 0) ~ (r2 ,0) 합 - (0, 0) ~ (0, c2) 합
+ (0, 0) 값 이 된다!

"""


R, C, Q = map(int, sys.stdin.readline().split())
MAP = [0] * R 
for i in range(0, R):
    MAP[i] = list(map(int, sys.stdin.readline().split()))

sum_arr = [[0] * C for _ in range(0, R)]

# 2차원 누적합 구하는법! 
# 열끼리 먼저 합을 구한후 => 해당 상태에서 행끼리 합을 구하면 됨!
# 아니면 반대로 (행끼리 먼저구한후 해당상태에서 열끼리 합)
# 우선 열끼리 합
for i in range(0, R):
    for j in range(0, C):
        if j == 0:
            sum_arr[i][j] = MAP[i][j]
        else:
            sum_arr[i][j] = sum_arr[i][j-1]+MAP[i][j]
# 해당 상태에서 행끼리 합
for j in range(0, C):
    for i in range(1, R):
        sum_arr[i][j] = sum_arr[i-1][j] + sum_arr[i][j]


for i in range(0, Q):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

    sum_1 = sum_arr[r2-1][c2-1]
    sum_2 = 0
    sum_3 = 0
    sum_4 = 0
    if c1 >= 2:
        sum_2 = sum_arr[r2-1][c1-2]
    if r1 >= 2:
        sum_3 = sum_arr[r1-2][c2-1]
    if r1 >= 2 and c1 >= 2:
        sum_4 = sum_arr[r1-2][c1-2]
    # 주의! 파이썬에서 음수 인덱스는 맨 뒤에서부터 접근하는것!
    # 그래서 sum_arr[-1][-1] 은 sum_arr[R-1][C-1] 이 되는것!
    sum_area = sum_1 - sum_2 - sum_3 + sum_4
    cell_cnt = (r2-r1+1)*(c2-c1+1)

    print(sum_area//cell_cnt)
