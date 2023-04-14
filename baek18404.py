import sys
sys.stdin = open("baek18404.txt")
from collections import deque


def bfs(k_row, k_col):

    visited = [[-1] * N for _ in range(0, N)]
    visited[k_row][k_col] = 0
    que = deque()
    que.append((k_row, k_col, 0))

    dr = [-1, -2, -2, -1, 1, 2, 2, 1]
    dc = [-2, -1, 1, 2, 2, 1, -1, -2]

    while que:
        row, col, path = que.popleft()

        for d in range(0, 8):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                continue
            if visited[next_row][next_col] == -1:
                visited[next_row][next_col] = path+1
                que.append((next_row, next_col, path+1))
    return visited


N, M = map(int, input().split())
knight_row, knight_col = map(int, input().split())

stones_pos = [0] * M
for i in range(0, M):
    r, c = map(int, input().split())
    stones_pos[i] = [r-1, c-1]

res_visited = bfs(knight_row-1, knight_col-1)
answer = [0] * M
for i in range(0, M):
    row, col = stones_pos[i]
    answer[i] = res_visited[row][col]
print(" ".join(map(str, answer)))