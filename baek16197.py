import sys
sys.stdin = open("baek16197.txt")
from collections import deque


def is_out_boundary(row, col):

    if row < 0 or col < 0 or row >= N or col >= M:
        return True
    return False


def find_min_req():
    
    check_dict = {}

    cnt = 0

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for row in range(0, N):
        for col in range(0, M):
            if MAP[row][col] == COIN:
                if cnt:
                    coin2_pos = [row, col]
                else:
                    coin1_pos = [row, col]
                    cnt += 1
    que = deque()
    que.append((coin1_pos[0], coin1_pos[1], coin2_pos[0], coin2_pos[1], 0))
    check_dict[(coin1_pos[0], coin1_pos[1], coin2_pos[0], coin2_pos[1])] = 1

    while que:
        coin1_row, coin1_col, coin2_row, coin2_col, time = que.popleft()
        
        # 최대 10번까지 허용
        if time == 10:
            continue
        for d in range(0, 4):
            flag_cnt = 0
            next_coin1_row = coin1_row + dr[d]
            next_coin1_col = coin1_col + dc[d]
            next_coin2_row = coin2_row + dr[d]
            next_coin2_col = coin2_col + dc[d]
            if is_out_boundary(next_coin1_row, next_coin1_col):
                flag_cnt += 1
            if is_out_boundary(next_coin2_row, next_coin2_col):
                flag_cnt += 1

            if flag_cnt == 1:
                return time+1
            if flag_cnt:
                continue
            # 벽이면 이동 안한다.
            if MAP[next_coin1_row][next_coin1_col] == WALL:
                next_coin1_row = coin1_row
                next_coin1_col = coin1_col
            if MAP[next_coin2_row][next_coin2_col] == WALL:
                next_coin2_row = coin2_row
                next_coin2_col = coin2_col
            next_check = (next_coin1_row, next_coin1_col, next_coin2_row, next_coin2_col)
            if next_check in check_dict.keys():
                continue
            check_dict[next_check] = 1
            # 같은포인트에 왔으면 pass 어떻게하던 같이떨어진다.
            if next_coin1_row == next_coin2_row and next_coin1_col == next_coin2_col:
                continue
            que.append((next_coin1_row, next_coin1_col, next_coin2_row, next_coin2_col, time+1))
    return -1

COIN = "o"
WALL = "#"
BLANK = "."

N, M = map(int, input().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(input())

answer = find_min_req()
print(answer)