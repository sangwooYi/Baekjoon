import sys
sys.stdin = open("baek21736.txt")
from collections import deque


def bfs():


    flag = False
    for row in range(0, N):
        for col in range(0, M):
            if MAP[row][col] == ME:
                start_row = row
                start_col = col
                flag = True
                break
        if flag:
            break
                

    visited = [[False] * M for _ in range(0, N)]
    visited[start_row][start_col] = True
    que = deque()
    que.append((start_row, start_col))


    cnt = 0
    while que:
        row, col = que.popleft()

        if MAP[row][col] == FRIEND:
            cnt += 1     

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
                continue
            if MAP[next_row][next_col] == WALL:
                continue            
            if visited[next_row][next_col]:
                continue
            visited[next_row][next_col] = True
            que.append((next_row, next_col))
    return cnt

BLANK = "O"
WALL = "X"
ME = "I"
FRIEND = "P"

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
MAP = [0] * N

for i in range(0, N):
    MAP[i] = list(input())


ans = bfs()
if ans == 0:
    print("TT")
else:
    print(ans)