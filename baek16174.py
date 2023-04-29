import sys
sys.stdin = open("baek16174.txt")
from collections import deque


def is_possible():

    visited = [[False] * N for _ in range(0, N)]
    dr = [1, 0]
    dc = [0, 1]

    que = deque()
    visited[0][0] = True
    que.append((0, 0))

    while que:
        row, col = que.popleft()

        if row == N-1 and col == N-1:
            return True
        cur_term = MAP[row][col]

        for d in range(0, 2):
            next_row = row + (dr[d]*cur_term)
            next_col = col + (dc[d]*cur_term)

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                continue
            if visited[next_row][next_col]:
                continue
            visited[next_row][next_col] = True
            que.append((next_row, next_col))
    return False

N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))

result = is_possible()

if result:
    print("HaruHaru")
else:
    print("Hing")