import sys
sys.stdin = open("baek14620.txt")


# 3개 다 꽃을 피울 수 있는 위치인지 확인
# 1. 전부 다른 위치여야 하고  2. 각 영역이 겹치면 안된다.  3. 5평을 빌릴 수 있어야 함
def is_possible(idx1, idx2, idx3):

    # 우선 겹치면 안된다
    if idx1 == idx2 or idx1 == idx3 or idx2 == idx3:
        return False
    
    tmp_arr = [idx1, idx2, idx3]
    
    for i in range(0, 3):
        for j in range(i+1, 3):
            r1, c1 = pos_points[tmp_arr[i]]
            r2, c2 = pos_points[tmp_arr[j]]

            # 딱 붙어있을때, 대각 1칸
            if abs(r1-r2) <= 1 and abs(c1-c2) <= 1:
                return False
            # row이 같은데 col이 2차이날 때, col이 같은데 row가 2차이 날 때
            if r1 == r2 and abs(c1-c2) == 2:
                return False
            if c1 == c2 and abs(r1-r2) == 2:
                return False
    for i in range(0, 3):
        row, col = pos_points[tmp_arr[i]]

        for d in range(0, 4):
            n_row = row + dr[d]
            n_col = col + dc[d]
            if n_row < 0 or n_col < 0 or n_row >= N or n_col >= N:
                return False

    return True


N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

arr_len = N*N
pos_points = [0] * arr_len
idx = 0

min_cost = 987654321
for r in range(0, N):
    for c in range(0, N):
        pos_points[idx] = [r, c]
        idx += 1

for i in range(0, arr_len):
    for j in range(0, arr_len):
        for k in range(0, arr_len):
            if is_possible(i, j, k):
                r1, c1 = pos_points[i]
                r2, c2 = pos_points[j]
                r3, c3 = pos_points[k]

                tmp_arr = [[r1, c1], [r2, c2], [r3, c3]]

                cur_total = 0
                for l in range(0, 3):
                    row, col = tmp_arr[l]
                    cur_total += MAP[row][col]

                    for d in range(0, 4):
                        n_row = row + dr[d]
                        n_col = col + dc[d]

                        cur_total += MAP[n_row][n_col]
                min_cost = min(min_cost, cur_total) 

print(min_cost)