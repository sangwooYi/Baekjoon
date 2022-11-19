import sys
sys.stdin = open("baek5549.txt")

"""
2차원에서 누적합 구하는 방법 익혀두자!!
"""

N, M = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(input())

idx_dict = {"J": 0, "O": 1, "I": 2}
count_arr = [[[0] * 3 for _ in range(0, M)] for _ in range(0, N)]

count_arr[0][0]
for row in range(0, N):
    for col in range(0, M):
        now = MAP[row][col]
        idx = idx_dict[now]
        count_arr[row][col][idx] +=1
        if row > 0:
            for k in range(0, 3):
                count_arr[row][col][k] += count_arr[row-1][col][k]

        if col > 0:
            for k in range(0, 3):
                count_arr[row][col][k] += count_arr[row][col-1][k]
        if row > 0 and col > 0:
            for k in range(0, 3):
                count_arr[row][col][k] -= count_arr[row-1][col-1][k]

for i in range(0, K):
    answer = [0, 0, 0]
    # (a, b)가 좌상단 / (c, d)가 우하단 즉 row 작은쪽이 a col도 작은쪽이 b
    a, b, c, d = map(int, sys.stdin.readline().split())
    
    for k in range(0, 3):
        answer[k] += count_arr[c-1][d-1][k]
        if  a > 1:
            answer[k] -= count_arr[a-2][d-1][k]
        if b > 1:
            answer[k] -= count_arr[c-1][b-2][k]
        if a > 1 and b > 1:
            answer[k] += count_arr[a-2][b-2][k]
    print(" ".join(map(str, answer)))
    