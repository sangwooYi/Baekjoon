import sys
import heapq
sys.stdin = open("baek1584.txt")


"""
0은 안전
1은 위험
2는 죽음으로 가면됨.
그리고 위험 => 죽음순으로 주어지기떄문에,
그냥 덮어 쓰면 된다.

맵 받은뒤에, 다잌스트라 진행 (가중치가 0과 1로 진행되는 다잌스트라임)
"""

def find_bfs():
    
    size = 501

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    INF = 987654321
    dist = [[INF] * size for _ in range(0, size)]
    dist[0][0] = 0
    hq = []

    heapq.heappush(hq, (0, 0, 0))

    while hq:
        cost, row, col = heapq.heappop(hq)

        if dist[row][col] < cost:
            continue

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= size or next_col >= size:
                continue
            if MAP[next_row][next_col] == 2:
                continue
            if MAP[next_row][next_col] == 1:
                next_cost = cost+1
            else:
                next_cost = cost
            if dist[next_row][next_col] <= next_cost:
                continue
            dist[next_row][next_col] = next_cost
            heapq.heappush(hq, (next_cost, next_row, next_col))
    if dist[size-1][size-1] == INF:
        return -1
    else:
        return dist[size-1][size-1]

# 기본 맵 501 * 501 사이즈로 고정
MAP = [[0] * 501 for _ in range(0, 501)]

N1 = int(input())
for i in range(0, N1):
    x1, y1, x2, y2 = map(int, input().split())
    
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)

    for row in range(min_y, max_y+1):
        for col in range(min_x, max_x+1):
            MAP[row][col] = 1
N2 = int(input())
for i in range(0, N2):
    x1, y1, x2, y2 = map(int, input().split())

    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)
    
    for row in range(min_y, max_y+1):
        for col in range(min_x, max_x+1):
            MAP[row][col] = 2

answer = find_bfs()
print(answer)