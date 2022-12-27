import sys
from collections import deque
sys.stdin = open("baek16509.txt")


"""
왕이 장애물일 수 있다. 주의하자!
"""

def bfs():
    dr = [[-1, -1, -1], [-1, -1, -1], [0, -1, -1], [0, 1, 1], [1, 1, 1], [1, 1, 1], [0, 1, 1], [0, -1, -1]]
    dc = [[0, 1, 1], [0, -1, -1], [1, 1, 1], [1, 1, 1], [0, -1, -1], [0, 1, 1], [-1, -1, -1], [-1, -1, -1]]
    visited = [[False] * COL for _ in range(0, ROW)]

    que = deque()
    visited[R1][C1] = True
    que.append((R1, C1, 0))
    
    while que:
        row, col, cnt = que.popleft()

        for d in range(0, 8):
            flag = True
            next_row = row
            next_col = col
            for k in range(0, 3):
                tmp_row = next_row + dr[d][k]
                tmp_col = next_col + dc[d][k]
                if tmp_row < 0 or tmp_col < 0 or tmp_row >= ROW or tmp_col >= COL:
                    flag = False
                    break
                # 이 문제에서 유일한 장애물 왕, 왕이 경로에 있으면 안된다.
                if k < 2 and tmp_row == R2 and tmp_col == C2:
                    flag = False
                    break
                next_row = tmp_row
                next_col = tmp_col
            if flag:
                if next_row == R2 and next_col == C2:
                    return cnt+1
                if visited[next_row][next_col]:
                    continue 
                visited[next_row][next_col] = True
                que.append((next_row, next_col, cnt+1))
    return -1

# 상의 위치
R1, C1 = map(int, input().split())
# 왕의 위치
R2, C2 = map(int, input().split())
ROW = 10
COL = 9

answer = bfs()
print(answer)
