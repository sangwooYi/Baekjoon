import sys
sys.stdin = open("baek2096.txt")
"""
오케이~~
"""


N = int(sys.stdin.readline())
DP_MAX = [[0] * 3 for _ in range(0, N)]
DP_MIN = [[0] * 3 for _ in range(0, N)] 
for row in range(0, N):
    temp = list(map(int, sys.stdin.readline().split()))
    if row == 0:
        DP_MAX[row] = temp
        DP_MIN[row] = temp
    else:
        for col in range(0, 3):
            if col == 0:
                DP_MAX[row][col] = max(DP_MAX[row-1][col], DP_MAX[row-1][col+1]) + temp[col]
                DP_MIN[row][col] = min(DP_MIN[row-1][col], DP_MIN[row-1][col+1]) + temp[col]
            elif col == 1:
                DP_MAX[row][col] = max(DP_MAX[row-1][col-1], DP_MAX[row-1][col], DP_MAX[row-1][col+1]) + temp[col]
                DP_MIN[row][col] = min(DP_MIN[row-1][col-1], DP_MIN[row-1][col], DP_MIN[row-1][col+1]) + temp[col]
            else:
                DP_MAX[row][col] = max(DP_MAX[row-1][col], DP_MAX[row-1][col-1]) + temp[col]
                DP_MIN[row][col] = min(DP_MIN[row-1][col], DP_MIN[row-1][col-1]) + temp[col]       

max_num = DP_MAX[N-1][0]
min_num = DP_MIN[N-1][0]
for i in range(1, 3):
    if max_num < DP_MAX[N-1][i]:
        max_num = DP_MAX[N-1][i]
    if min_num > DP_MIN[N-1][i]:
        min_num = DP_MIN[N-1][i]
# f프린트!
print(f"{max_num} {min_num}")
    