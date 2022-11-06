import sys
from collections import deque
sys.stdin = open("baek6087.txt")


"""
다익스트라 기본은
가중치가 존재하는 간선에서
최소 cost를 사용하여 출발 -> 목적 노드까지 가는
경로를 찾는 알고리즘!
(heapq, 즉 우선순위 큐를 사용한다.)
근데 만약 가중치가 존재하지 않는 경우라면
사실 BFS 로 진행해도 같은 결과임.

거울을 설치하면 
반시계 or 시계방향으로 90도 꺾을 수 있다.
따라서 델타함수를
북 동 남 서 순서로 선언해야함

현재 델타함수 인덱스를 d라고 할때
시계방향은 (d+1)%4
반시계방향은 (d+4-1)%4 로 표현 가능
"""

def find_min(arr):
    r = len(arr)
    c = len(arr[0])
    wall = "*"
    # 북 동 남 서
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    INF = 987654

    # 거울을 사용한 횟수를 체크함
    dist = [[INF] * c for _ in range(0, r)]

    cnt = 0
    for row in range(0, r):
        if cnt == 2:
            break
        for col in range(0, c):
            if cnt == 2:
                break
            if arr[row][col] == "C":
                if cnt:
                    target_row = row
                    target_col = col
                else:
                    start_row = row
                    start_col = col
                cnt += 1 
    dist[start_row][start_col] = 0

    que = deque()

    # 처음에 출발방향은 다 따져보아야 한다.
    for d in range(0, 4):
        next_row = start_row + dr[d]
        next_col = start_col + dc[d]
        if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
            continue
        if arr[next_row][next_col] == wall:
            continue
        # row 좌표, col 좌표, 방향, 거울 사용 갯수
        que.append((next_row, next_col, d, 0))
        dist[next_row][next_col] = 0

    while que:
        row, col, direct, count = que.popleft()
        # 반시계 / 유지 / 시계방향 총 3가지 경우가 매번 발생
        for k in range(-1, 2):
            if k == -1:
                next_d = (direct+4-1)%4
                next_cnt = count + 1
            elif k == 1:
                next_d = (direct+1)%4
                next_cnt = count + 1
            else:
                next_d = direct
                next_cnt = count
            next_row = row + dr[next_d]
            next_col = col + dc[next_d]

            if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
                continue
            if arr[next_row][next_col] == wall:
                continue
            # 같은 cost로 방문한 case를 일단 살려두는 것이 point!
            # 일반적인 4방향 델타함수 탐색이 아니기에,
            # 해당 지점에 같은 cost로 도달한 이후에도 다른 방향으로 진행 가능하기때문 
            # 그냥 인접지점으로 이동하는 일반적인 문제는 DP 개념이 적용되어 어차피 
            # 해당 지점까지 도착하고 나면 그다음 경로의 case가 동일하다. 따라서 같은 cost도 잘라버리는것!! 
            if dist[next_row][next_col] < next_cnt:
                continue
            dist[next_row][next_col] = next_cnt
            que.append((next_row, next_col, next_d, next_cnt))
    return dist[target_row][target_col]
# W 가 column / H 가 row
W, H = map(int, input().split())

MAP = [0] * H
for i in range(0, H):
    MAP[i] = list(input())

answer = find_min(MAP)
print(answer)