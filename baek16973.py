import sys
from collections import deque
sys.stdin = open("baek16973.txt")

"""
ul, ur, dl, dr 각 모서리가 있을때
움직일때 따져야할 범위
왼쪽: ul~dl
오른쪽: ur~dr
위쪽: ul~ur
아래쪽 dl~dr

따라서 최대 1000회씩의 연산이 발생
맵도 최대 1000*1000 = 잘모하면 시간초과 날듯..????
최대 10억회라 통과할것같긴 한데
"""

def is_over_range(row, col):
    if row < 0 or col < 0 or row >= N or col >= M:
        return True
    return False

def bfs():
    visited = [[False] * M for _ in range(0, N)]
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 가장 왼쪽 위칸 기준으로 진행
    visited[SR][SC] = True
    que = deque()
    que.append((SR, SC, 0))

    UP = 0
    DOWN = 1
    LEFT = 2
    while que:
        row, col, cnt = que.popleft()

        if row == FR and col == FC:
            return cnt

        for d in range(0, 4):
            tmp_row = row + dr[d]
            tmp_col = col + dc[d]

            if is_over_range(tmp_row, tmp_col):
                continue
            if visited[tmp_row][tmp_col]:
                continue
            flag = True
            if d == UP:
                for k in range(0, W):
                    next_row = tmp_row
                    next_col = tmp_col+k
                    if is_over_range(next_row, next_col):
                        flag = False
                        break
                    if MAP[next_row][next_col]:
                        flag = False
                        break
            elif d == DOWN:
                for k in range(0, W):
                    next_row = tmp_row+(H-1)
                    next_col = tmp_col+k
                    if is_over_range(next_row, next_col):
                        flag = False
                        break
                    if MAP[next_row][next_col]:
                        flag = False
                        break                    
            elif d == LEFT:
                for k in range(0, H):
                    next_row = tmp_row+k
                    next_col = tmp_col
                    if is_over_range(next_row, next_col):
                        flag = False
                        break
                    if MAP[next_row][next_col]:
                        flag = False
                        break                    
            # RIGHT
            else:
                for k in range(0, H):
                    next_row = tmp_row+k
                    next_col = tmp_col+(W-1)
                    if is_over_range(next_row, next_col):
                        flag = False
                        break
                    if MAP[next_row][next_col]:
                        flag = False
                        break
            if flag:
                if tmp_row == FR and tmp_col == FC:
                    return cnt+1                
                visited[tmp_row][tmp_col] = True
                que.append((tmp_row, tmp_col, cnt+1))
    return -1

N, M = map(int, sys.stdin.readline().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, sys.stdin.readline().split()))
H, W, SR, SC, FR, FC = map(int, sys.stdin.readline().split())
# 실제 좌표로 연동
SR -= 1
SC -= 1
FR -= 1
FC -= 1
answer = bfs()
print(answer)