import sys
sys.stdin = open("baek13903.txt")
from collections import deque


def bfs():

    visited = [[-1] * C for _ in range(0, R)]
    
    que = deque()
    for i in range(0, C):
        if MAP[0][i]:
            visited[0][i] = 0
            que.append((0, i, 0))
    
    while que:
        row, col, path = que.popleft()

        for d in range(0, N):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= R or next_col >= C:
                continue
            # 아직 방문 안한 애들부터, 그리고 가려는 위치가 세로 블록이어야 함
            if visited[next_row][next_col] == -1 and MAP[next_row][next_col]:
                if next_row == R-1:
                    return path+1
                visited[next_row][next_col] = path+1
                que.append((next_row, next_col, path+1))
    return -1


R, C = map(int, input().split())
MAP = [0] * R
for i in range(0, R):
    MAP[i] = list(map(int, input().split()))

N = int(input())
dr = [0] * N
dc = [0] * N
for i in range(0, N):
    row, col = map(int, input().split())
    dr[i] = row
    dc[i] = col

answer = bfs()
print(answer)