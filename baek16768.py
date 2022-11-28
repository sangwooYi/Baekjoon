import sys
from collections import deque
sys.stdin = open("baek16768.txt")


def bfs(arr, r, c, k):
    n = len(arr)
    n_c = len(arr[0])
    que = deque()
    tmp_que = deque()
    
    que.append((r, c))
    tmp_que.append((r, c))

    cnt = 1
    color = arr[r][c]
    while que:
        row, col = que.popleft()

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n_c:
                continue
            if visited[next_row][next_col]:
                continue
            if arr[next_row][next_col] != color:
                continue
            visited[next_row][next_col] = True
            cnt += 1
            que.append((next_row, next_col))
            tmp_que.append((next_row, next_col))

    if cnt >= k:
        while tmp_que:
            row, col = tmp_que.popleft()
            arr[row][col] = 0
        return True
    return False

# 정사각형 아니다...
N, K = map(int, input().split())
MAP = [0] * N

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(0, N):
    MAP[i] = list(map(int, input()))

C = len(MAP[0])
while True:

    visited = [[False] * C for _ in range(0, N)]
    
    flag = False
    for row in range(0, N):
        for col in range(0, C):
            if MAP[row][col] != 0 and not visited[row][col]:
                visited[row][col] = True
                res = bfs(MAP, row, col, K)
                # 한번이라도 T가 나오면
                if res:
                    flag = True

    if not flag:
        break
    
    # 재배치
    tmp = [[0] * C for _ in range(0, N)]

    for col in range(0, C):
        idx = N-1
        for row in range(N-1, -1, -1):
            if MAP[row][col] != 0:
                tmp[idx][col] = MAP[row][col]
                idx -= 1
    MAP = tmp
for i in range(0, N):
    print("".join(map(str, MAP[i])))