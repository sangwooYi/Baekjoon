import sys
from collections import deque
sys.stdin = open("baek17142.txt")

"""
0은 빈칸, 1은 벽, 2는 바이러스를 놓을 수 있는 공간
2의 갯수는 M 이상이고 // 10 이하이다.

+ 동시에 퍼지므로 이부분을 주의해야함!
"""


def bfs(arr, box):
    n = len(box)

    que = deque()
    visited = [[False] * n for _ in range(0, n)]


    for i in range(0, len(arr)):
        row, col = arr[i]
        visited[row][col] = True
        que.append((row, col))

    safe_zone = 0
    for row in range(0, n):
        for col in range(0, n):
            if box[row][col] == 0:
                safe_zone += 1

    time = 0
    while True:
        if safe_zone == 0:
            return time
        if len(que) == 0:
            return INF
        tmp_que = deque()

        while que:
            row, col = que.popleft()

            for d in range(0, 4):
                next_row = row + dr[d]
                next_col = col + dc[d]

                if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n:
                    continue
                if box[next_row][next_col] == 1:
                    continue
                if visited[next_row][next_col]:
                    continue
                if box[next_row][next_col] == 0:
                    safe_zone -= 1
                visited[next_row][next_col] = True
                tmp_que.append((next_row, next_col))
        while tmp_que:
            row, col = tmp_que.popleft()
            que.append((row, col))
        time += 1


def comb(arr, visited, start, n, r, k, box):
    global answer

    if r == 0:
        tmp = [0] * k
        idx = 0
        for i in range(0, n):
            if visited[i]:
                tmp[idx] = arr[i]
                idx += 1
        time = bfs(tmp, box)
        answer = min(answer, time)
        return
    for i in range(start, n):
        if visited[i]:
            continue
        visited[i] = True
        comb(arr, visited, i+1, n, r-1, k, box)
        visited[i] = False


# N은 맵 크기 (정사각형), M은 바이러스 갯수
N, M = map(int, input().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))

possible_pos = []
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
INF = 987654321
answer = INF

for row in range(0, N):
    for col in range(0, N):
        if MAP[row][col] == 2:
            possible_pos.append((row, col))

visited = [False] * len(possible_pos)

comb(possible_pos, visited, 0, len(possible_pos), M, M, MAP)

if answer == INF:
    answer = -1
print(answer)