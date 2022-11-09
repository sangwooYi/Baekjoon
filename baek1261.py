import sys
from collections import deque
sys.stdin = open("baek1261.txt")



def algo_spot(arr):

    r = len(arr)
    c = len(arr[0])

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    que = deque()
    INF = 987654321
    dist = [[INF] * c for _ in range(0, r)]
    dist[0][0] = 0
    que.append((0, 0, 0))

    while que:
        row, col, cnt = que.popleft()

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
                continue
            next_cnt = cnt
            if arr[next_row][next_col]:
                next_cnt = cnt+1

            if dist[next_row][next_col] <= next_cnt:
                continue
            dist[next_row][next_col] = next_cnt
            que.append((next_row, next_col, next_cnt))
    
    return dist[r-1][c-1]

M, N = map(int, input().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input()))


answer = algo_spot(MAP)
print(answer)