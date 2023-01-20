import sys
import heapq
sys.stdin = open("baek20046.txt")


def dijkstra():

    hq = []
    INF = 987654321
    start_cost = MAP[0][0]
    # 시작점이 -1일수도 있다! 문제 잘 읽을것
    if start_cost == -1:
        return -1
    dist = [[INF] * N for _ in range(0, M)]
    dist[0][0] = start_cost

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1 ,1]
    heapq.heappush(hq, (start_cost, 0, 0))

    while hq:
        cost, row, col = heapq.heappop(hq)

        if dist[row][col] < cost:
            continue
        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= M or next_col >= N:
                continue
            if MAP[next_row][next_col] == -1:
                continue
            next_cost = MAP[next_row][next_col]

            if dist[next_row][next_col] <= cost + next_cost:
                continue
            dist[next_row][next_col] = cost + next_cost
            heapq.heappush(hq, (dist[next_row][next_col], next_row, next_col))
    if dist[M-1][N-1] == INF:
        return -1
    else:
        return dist[M-1][N-1]

# M이 행, N이 열
M, N = map(int, sys.stdin.readline().split())
MAP = [0] * M
for i in range(0, M):
    MAP[i] = list(map(int, sys.stdin.readline().split()))

answer = dijkstra()
print(answer)