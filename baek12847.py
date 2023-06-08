import sys
sys.stdin = open("baek12847.txt")


N, M = map(int, sys.stdin.readline().split())
pay_infos = list(map(int, sys.stdin.readline().split()))

sum_arr = [0] * N
sum_arr[0] = pay_infos[0]
for i in range(1, N):
    sum_arr[i] = sum_arr[i-1]+pay_infos[i]

answer = 0

# 슬라이딩 윈도우
for start_idx in range(0, N-M+1):
    end_idx = start_idx+M-1

    cur_paid = sum_arr[end_idx]
    if start_idx > 0:
        cur_paid -= sum_arr[start_idx-1]
    answer = max(answer, cur_paid)
print(answer)