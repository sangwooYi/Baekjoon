import sys
sys.stdin = open("baek11660.txt")
"""
아래처럼 해도 시간초과네 ㅡㅡ?
이거 어떻게하면 시간 줄일지 고민좀 해보자

최대 1억번이라서, 가능할것같기도..
"""

N, M = map(int, sys.stdin.readline().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, sys.stdin.readline().split()))
sum_arr = [0] * N
for i in range(0, N):
    temp = [0] * N
    sum = 0
    for j in range(0, N):
        sum += MAP[i][j]
        temp[j] = sum
    sum_arr[i] = temp


for i in range(0, M):
    x1, y1, x2, y2 = list(map(int, sys.stdin.readline().split()))
    # 문제는 1행 / 1열부터 시작 따라서 1씩 빼줘야함
    total = 0
    for j in range(x1-1, x2):
        if y1 == 1:
            temp_sum = sum_arr[j][y2-1]
        else:
            temp_sum = (sum_arr[j][y2-1] - sum_arr[j][y1-2])
        total += temp_sum
    print(total)