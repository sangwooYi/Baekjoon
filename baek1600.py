import sys
sys.stdin = open("baek1600.txt")
from collections import deque

""" 
벽 깨부수는 문제와 같다!
"""


def find_min_req():
    # 그냥 1*1인 경우
    if H == 1 and W == 1:
        return 0
    que = deque()
    # 일접한방향 상하좌우
    normal = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # 말의 움직임
    horse = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]


    visited = [[[0] * (K+1) for _ in range(0, W)] for _ in range(0, H)]
    visited[0][0][0] = 0
    que.append((0, 0, K))

    while que:
        row, col, time = que.popleft()   
        
        if row == H-1 and col == W-1:
            return visited[row][col][time]

        if time > 0:
            for d in range(0, 8):
                next_row = row + horse[d][0]
                next_col = col + horse[d][1]

                if next_row < 0 or next_col < 0 or next_row >= H or next_col >= W:
                    continue
                if MAP[next_row][next_col]:
                    continue
                if visited[next_row][next_col][time-1]:
                    continue
                visited[next_row][next_col][time-1] = visited[row][col][time]+1
                que.append((next_row, next_col, time-1))
        for d in range(0, 4):
            next_row = row + normal[d][0]
            next_col = col + normal[d][1]
            if next_row < 0 or next_col < 0 or next_row >= H or next_col >= W:
                continue
            if MAP[next_row][next_col]:
                continue
            if visited[next_row][next_col][time]:
                continue
            visited[next_row][next_col][time] = visited[row][col][time]+1
            que.append((next_row, next_col, time))

    return -1

K = int(input())
# 가로, 세로
W, H = map(int, input().split())
MAP = [0] * H
for i in range(0, H):
    MAP[i] = list(map(int, input().split()))

answer = find_min_req()
print(answer)