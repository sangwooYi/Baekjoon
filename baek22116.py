import sys
import heapq
sys.stdin = open("baek22116.txt")


N = int(sys.stdin.readline().rstrip())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, sys.stdin.readline().split()))

INF = 987654321
DP = [[INF] * N for _ in range(0, N)]


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
hq = []
DP[0][0] = 0
# cost 기준 최소힙 진행
heapq.heappush(hq, [0, 0, 0])

while hq:

    cost, row, col = heapq.heappop(hq)

    for d in range(0, 4):
        next_row = row + dr[d]
        next_col = col + dc[d]

        if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
            continue
        next_slide = abs(MAP[row][col]-MAP[next_row][next_col])
        next_cost = max(cost, next_slide)
        if DP[next_row][next_col] <= next_cost:
            continue
        DP[next_row][next_col] = next_cost
        heapq.heappush(hq, [next_cost, next_row, next_col])
print(DP[N-1][N-1])


