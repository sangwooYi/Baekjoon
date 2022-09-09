import sys
import heapq
sys.stdin = open("baek4485.txt")


def zelda(arr):

    n = len(arr)
    hq = []
    INF = 987654321
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    dst = [[INF] * n for _ in range(0, n)]
    dst[0][0] = arr[0][0]
    heapq.heappush(hq, (0, 0))

    while hq:
        row, col = heapq.heappop(hq)

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]
            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n:
                continue
            # 경로상 이득이 있을때만 이동
            if dst[next_row][next_col] <= dst[row][col] + arr[next_row][next_col]:
                continue
            dst[next_row][next_col] = dst[row][col] + arr[next_row][next_col]
            heapq.heappush(hq, (next_row, next_col))
    return dst[n-1][n-1]

tc = 1
while True:

    N = int(input())
    if N == 0:
        break
    MAP = [0] * N
    for i in range(0, N):
        MAP[i] = list(map(int, input().split()))

    answer = zelda(MAP)
    # f 스트링 유용하게 쓰자!
    print(f'Problem {tc}: {answer}')
    tc += 1