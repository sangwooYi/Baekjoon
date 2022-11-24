import sys
from collections import deque
sys.stdin = open("baek2151.txt")

"""

45도 기울어져 있는 거울의 의미
-> / <- 를 위나 아래로
위/ 아래를 -> / <- 로 방향을 틀 수 있음!

거울문제 주의할점!

일반 다익스트라/BFS랑 다르게
현재 점을 지나갈때 기존 저장값보다 큰값일지라도 최종 결과에서는 최솟값인 경우가 존재!
=> 따라서 각 포인트마다, 방향에 따른 dist값을 체크해주어야 함! 이부분 주의!
"""

def is_over(row, col, n):
    if row < 0 or col < 0 or row >= n or col >= n:
        return True
    return False


def min_req(arr):

    n = len(arr)
    INF = 987654321
    que = deque()

    wall = "*"
    pos_place = "!"
    empty = "."

    # 상 우 하 좌 (거울 방향전환 체크를 쉽게 하기 위함)
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # 해당 위치까지 이동하는데 필요한 최소 거울 갯수
    dist = [[[INF] * 4 for _ in range(0, n)] for _ in range(0, n)]

    cnt = 0
    for row in range(0, n):
        if cnt > 2:
            break
        for col in range(0, n):
            if arr[row][col] == "#":
                if cnt > 1:
                    break
                if cnt:
                    end_row = row
                    end_col = col
                else:
                    start_row = row
                    start_col = col
                cnt += 1
    # 우선 출발지에서 네방향중 가능한방향 전부 탐색
    for d in range(0, 4):
        next_row = start_row + dr[d]
        next_col = start_col + dc[d]
        dist[start_row][start_col][d] = 0
        if is_over(next_row, next_col, n):
            continue
        if arr[next_row][next_col] == wall:
            continue
        # 바로 도착할 수 있으면 즉시 종료
        if next_row == end_row and next_col == end_col:
            return 0
        if arr[next_row][next_col] == empty:
            dist[next_row][next_col][d] = 0
            que.append((next_row, next_col, d, 0))
        
        if arr[next_row][next_col] == pos_place:
            for k in range(-1, 2):
                next_d = d + k
                if next_d == 4:
                    next_d = 0
                elif next_d == -1:
                    next_d = 3
                next_row = start_row + dr[next_d]
                next_col = start_col + dc[next_d]
                if is_over(next_row, next_col, n):
                    continue
                if arr[next_row][next_col] == wall:
                    continue
                if k == 0:
                    next_cnt = 0
                else:
                    next_cnt = 1
                dist[next_row][next_col][next_d] = next_cnt
                que.append((next_row, next_col, next_d, next_cnt))

    while que:
        row, col, now_d, cnt = que.popleft()

        # 방향 유지
        if arr[row][col] == empty:
            next_row = row + dr[now_d]
            next_col = col + dc[now_d]

            if is_over(next_row, next_col, n):
                continue
            if arr[next_row][next_col] == wall:
                continue
            if dist[next_row][next_col][now_d] < cnt:
                continue
            dist[next_row][next_col][now_d] = cnt
            if next_row == end_row and next_col == end_col:
                continue
            que.append((next_row, next_col, now_d, cnt))
        
        # 좌회전 / 유지 / 우회전 3가지!
        if arr[row][col] == pos_place:

            for k in range(-1, 2):
                next_d = now_d + k
                if next_d == 4:
                    next_d = 0
                elif next_d == -1:
                    next_d = 3
                next_row = row + dr[next_d]
                next_col = col + dc[next_d]
                if is_over(next_row, next_col, n):
                    continue
                if arr[next_row][next_col] == wall:
                    continue
                if k == 0:
                    next_cnt = cnt
                else:
                    next_cnt = cnt+1
                if dist[next_row][next_col][next_d] < next_cnt:
                    continue
                dist[next_row][next_col][next_d] = next_cnt
                if next_row == end_row and next_col == end_col:
                    continue                
                que.append((next_row, next_col, next_d, next_cnt))                
    return min(dist[end_row][end_col])


N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(input())


answer = min_req(MAP)
print(answer)