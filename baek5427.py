import sys
from collections import deque
sys.stdin = open("baek5427.txt")


def bfs(arr):

    r = len(arr)
    c = len(arr[0])

    visited = [[False] * c for _ in range(0, r)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    que = deque()
    fire_que = deque()

    for i in range(0, r):
        for j in range(0, c):
            if arr[i][j] == "@":
                start_row = i
                start_col = j
            if arr[i][j] == "*":
                fire_que.append((i, j))
    que.append((start_row, start_col))
    visited[start_row][start_col] = True
    
    time = 0
    while True:
        time += 1

        tmp = []
        while fire_que:
            row, col = fire_que.popleft()

            for d in range(0, 4):
                next_row = row + dr[d]
                next_col = col + dc[d]

                if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
                    continue
                if arr[next_row][next_col] == "#":
                    continue
                if arr[next_row][next_col] == "*":
                    continue
                arr[next_row][next_col] = "*"
                tmp.append((next_row, next_col))

        for i in range(0, len(tmp)):
            fire_que.append(tmp[i])

        tmp = []
        while que:
            row, col = que.popleft()
            
            for d in range(0, 4):
                next_row = row + dr[d]
                next_col = col + dc[d]

                # 탈출 성공
                if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
                    return time
                if arr[next_row][next_col] == "#":
                    continue
                if arr[next_row][next_col] == "*":
                    continue 
                if visited[next_row][next_col]:
                    continue
                visited[next_row][next_col] = True
                tmp.append((next_row, next_col))
        if not tmp:
            break
        for i in range(0, len(tmp)):
            que.append((tmp[i]))


    
    return "IMPOSSIBLE"


T = int(input())
for tc in range(0, T):
    # 열, 행
    W, H = map(int, input().split())
    MAP = [0] * H
    for i in range(0, H):
        MAP[i] = list(input())
    
    answer = bfs(MAP)
    print(answer)