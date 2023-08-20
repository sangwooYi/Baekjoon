#N = int(input())
#NUM = int(input())

def is_out_boundary(r, c):

    if r < 0 or c < 0 or r >= N or c >= N:
        return True
    return False


N = 7
NUM = 35

MAP = [[0] * N for _ in range(0, N)]
visited = [[False] * N for _ in range(0, N)]
# 하 우 상 좌
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

d = 0
row = 0
col = 0
cur_num = N*N

while cur_num > 0:

    MAP[row][col] = cur_num
    visited[row][col] = True

    cur_num -= 1
    next_row = row + dr[d]
    next_col = col + dc[d]

    if is_out_boundary(next_row, next_col) or visited[next_row][next_col]:
        d = (d + 1)%4
        row = row + dr[d]
        col = col + dc[d]
        continue
    row = next_row
    col = next_col

for i in range(0, N):
    print(" ".join(map(str, MAP[i])))


flag = False
for r in range(0, N):
    for c in range(0, N):
        if MAP[r][c] == NUM:
            print(r+1, c+1)
            flag = True
            break
    if flag:
        break