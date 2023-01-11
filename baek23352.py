import sys
sys.stdin = open("baek23352.txt")
from collections import deque

"""
출발점만 체크하면 된다!!!!!
"""

def bfs(start):
    visited = [[False] * M for _ in range(0, N)]
    visited[start[0]][start[1]] = True
    que = deque()
    que.append((start[0], start[1], 0))
    

    max_path = 0
    start_point = MAP[start[0]][start[1]]
    now_sum = 2*start_point
    while que:
        row, col, path = que.popleft()
        

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
                continue
            if MAP[next_row][next_col] == 0:
                continue
            if visited[next_row][next_col]:
                continue
            visited[next_row][next_col] = True
            if max_path < path+1:
                now_sum = start_point+MAP[next_row][next_col]
                max_path = path+1
            elif max_path == path+1:
                now_sum = max(now_sum, start_point+MAP[next_row][next_col])            
            que.append((next_row, next_col, path+1))
    return (max_path, now_sum)


# 1 <= N, M <= 50 N이 세로, M이 가로
N, M = map(int, input().split())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))


max_path = 0
answer = 0
for row in range(0, N):
    for col in range(0, M):
        if MAP[row][col]:
            now_path, now_sum = bfs((row, col))
            
            if now_path > max_path:
                answer = now_sum
                max_path = now_path
            elif now_path == max_path:
                answer = max(answer, now_sum)
print(answer)