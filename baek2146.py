import sys
from collections import deque
sys.stdin = open("baek2146.txt")

"""
N 이 최대 100이므로, 복잡한 연산도 충분히 가능 (100*100)

그래도 효율적이게 해야한다.
방법은 맞았는데.. 내 코드가 효율이 안좋아서 계속 시간 초과가 난 문제...
"""

def bfs(r, c):
    global cnt
    que = deque()

    visited[r][c] = True
    que.append((r, c))
    MAP[r][c] = cnt
    while que:
        row, col = que.popleft()

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                continue
            if visited[next_row][next_col]:
                continue
            if MAP[next_row][next_col] == 0:
                continue
            visited[next_row][next_col] = True
            MAP[next_row][next_col] = cnt
            que.append((next_row, next_col))


def bfs2(num):
    global result
    
    que = deque()
    dp = [[-1] * N for _ in range(0, N)]

    for i in range(0, N):
        for j in range(0, N):
            if MAP[i][j] == num:
                que.append((i, j))
                dp[i][j] = 0
    while que:
        row, col = que.popleft()

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                continue
            if MAP[next_row][next_col] > 0 and MAP[next_row][next_col] != num:
                result = min(result, dp[row][col])
                return
            if MAP[next_row][next_col] == 0 and dp[next_row][next_col] == -1:
                dp[next_row][next_col] = dp[row][col] + 1
                que.append((next_row, next_col))

N = int(sys.stdin.readline())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, sys.stdin.readline().split()))

result = 10000
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
visited = [[False] * N for _ in range(0, N)]
cnt = 1

for i in range(0, N):
    for j in range(0, N):
        if not visited[i][j] and MAP[i][j] > 0:
            bfs(i, j)
            cnt += 1

for i in range(1, cnt):
    bfs2(i)

print(result)