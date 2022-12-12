import sys
from collections import deque
sys.stdin = open("baek16469.txt")


"""
R/C <= 100 따라서 시간적으로는 여유있음!
"""

def find_min():


    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    

    visited = [[[False] * 3 for _ in range(0, C)] for _ in range(0, R)]

    que_list = [0] * 3
    
    for i in range(0, 3):
        row, col = billons[i]
        row -= 1
        col -= 1
        visited[row][col][i] = True

        que = deque()

        que.append((i, row, col, 0))
        que_list[i] = que

    end_flag = False

    req_time = 0
    pos_cnt = 0
    # 위치가 겹치게 주어지는 경우는 없다. 
    while not end_flag:
        
        tmp_flag = False

        for i in range(0, 3):
            now_que = que_list[i]
            
            tmp_que = deque()
            while now_que:
                code, row, col, time = now_que.popleft()
                for d in range(0, 4):
                    next_row = row + dr[d]
                    next_col = col + dc[d]

                    if next_row < 0 or next_col < 0 or next_row >= R or next_col >= C:
                        continue
                    if MAP[next_row][next_col]:
                        continue
                    if visited[next_row][next_col][code]:
                        continue
                    visited[next_row][next_col][code] = True

                    # 모두가 모인 경우
                    if visited[next_row][next_col][0] and visited[next_row][next_col][1] and visited[next_row][next_col][2]:
                        end_flag = True
                        req_time = time+1
                        pos_cnt += 1
                        continue
                    tmp_que.append((code, next_row, next_col, time+1))
            
            if tmp_que:
                tmp_flag = True
                next_que = deque()
                while tmp_que:
                    tmp = tmp_que.popleft()
                    next_que.append(tmp)
                que_list[i] = next_que

        # 0, 1, 2번 모두 더이상 진행이 안되는 상태
        if not tmp_flag:
            break
    if end_flag:
        return (req_time, pos_cnt)
    else:
        return -1

R, C = map(int, input().split())
MAP = [0] * R
for i in range(0, R):
    MAP[i] = list(map(int, input()))

billons = [0] * 3
for i in range(0, 3):
    billons[i] = list(map(int, input().split()))


answer = find_min()

if answer == -1:
    print(-1)
else:
    print(answer[0])
    print(answer[1])