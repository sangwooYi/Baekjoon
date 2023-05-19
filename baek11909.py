import sys
from collections import deque
sys.stdin = open("baek11909.txt")


def find_min_cost():
    # 우, 하로만 이동 가능
    dr = [1, 0]
    dc = [0, 1]
    INF = 987654321
    DP = [[INF] * N for _ in range(0, N)]
    que = deque()
    DP[0][0] = 0
    que.append((0, 0))

    while que:
        row, col = que.popleft()

        for d in range(0, 2):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                continue
            req_cost = 0
            if MAP[next_row][next_col] >= MAP[row][col]:
                # 가려는 경로보다 현재값이 더 커야만 한다.
                req_cost = MAP[next_row][next_col]-MAP[row][col]+1 
            # 현재 가려는 경로가 저장된값보다 크거나 같으면 굳이 진행 X
            if DP[next_row][next_col] <= DP[row][col] + req_cost:
                continue
            DP[next_row][next_col] = DP[row][col] + req_cost
            que.append((next_row, next_col))
    return DP[N-1][N-1]
"""
굳이 dijkstra 필요 없는 문제..  
그냥 DP[r][c] <= r, c 까지 이동하는데 필요한 최소비용

"""


N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))

answer = find_min_cost()
print(answer)