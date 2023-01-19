import sys
import heapq
sys.stdin = open("baek9505.txt")


def find_start_point():

    for row in range(0, H):
        for col in range(0, W):
            if MAP[row][col] == "E":
                return (row, col)
    


def dijkstra():

    dist = [[INF] * W for _ in range(0, H)]

    start_point = find_start_point()
    hq = []
    dist[start_point[0]][start_point[1]] = 0

    heapq.heappush(hq, (0, start_point[0], start_point[1]))
    while hq:
        cost, row, col = heapq.heappop(hq)
        # 이경우 바로 리턴해도 괜찮다! 어차피 최소힙으로 현재 값으로 가장먼저 도달하는값이 최소비용일것!
        if row == 0 or col == 0 or row == H-1 or col == W-1:
            return cost

        if dist[row][col] < cost:
            continue
        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= H or next_col >= W:
                continue
            next_cost = req_time[MAP[next_row][next_col]]
            if dist[next_row][next_col] <= cost + next_cost:
                continue
            dist[next_row][next_col] = cost + next_cost
            heapq.heappush(hq, (dist[next_row][next_col], next_row, next_col))


INF = 9876543219
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
T = int(sys.stdin.readline())
for tc in range(0, T):
    K, W, H = map(int, sys.stdin.readline().split())
    req_time = {}
    # 클래스이름 어차피 안겹친다.
    for i in range(0, K):
        alph, time = sys.stdin.readline().split()
        req_time[alph] = int(time)
    req_time["E"] = 0
    MAP = [0] * H
    for i in range(0, H):
        MAP[i] = list(sys.stdin.readline().rstrip())

    answer = dijkstra()
    print(answer)