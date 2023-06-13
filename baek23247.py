import sys
sys.stdin = open("baek23247.txt")


R, C = map(int, input().split())
MAP = [0] * R
for i in range(0, R):
    MAP[i] = list(map(int, input().split()))


sum_arr = [[0] * C for _ in range(0, R)]

for i in range(0, R):
    for j in range(0, C):
        if j == 0:
            sum_arr[i][j] = MAP[i][j]
        else:
            sum_arr[i][j] = sum_arr[i][j-1]+MAP[i][j]

for j in range(0, C):
    for i in range(1, R):
        sum_arr[i][j] = sum_arr[i][j] + sum_arr[i-1][j]


cnt = 0
# 이때부터 브루트 포스 진행

# i,j 부터 k,l 까지의 부분합을 구하며 => 10이 넘어가는 순간 종료 (모두 양수이므로)
# 따라서 가로,세로 각각 최대 10칸까지 가능 (가장 작은 값이 1이므로)
for i in range(0, R):
    for j in range(0, C):
        for k in range(i, i+10):
            for l in range(j, j+10):
                if k >= R or l >= C:
                    continue
                cur_sum = sum_arr[k][l]
                if j > 0:
                    cur_sum -= sum_arr[k][j-1]
                if i > 0:
                    cur_sum -= sum_arr[i-1][l]
                if i > 0 and j > 0:
                    cur_sum += sum_arr[i-1][j-1]
                if cur_sum == 10:
                    cnt += 1
print(cnt)