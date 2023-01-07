import sys
from collections import deque
sys.stdin = open("baek17141.txt")


def deep_copy(arr):
    tmp_arr = [[0] * N for _ in range(0, N)]

    for row in range(0, N):
        for col in range(0, N):
            tmp_arr[row][col] = arr[row][col]
    return tmp_arr

def bfs(start_arr, lab_map):
    
    copy_map = deep_copy(lab_map)

    visited = [[False] * N for _ in range(0, N)]


    que = deque()
    for i in range(0, len(start_arr)):
        row, col = start_arr[i]
        que.append((row, col))
        copy_map[row][col] = VIRUS
        visited[row][col] = True
    
    req_time = 0

    while True:    
        flag = True
        for row in range(0, N):
            if not flag:
                break
            for col in range(0, N):
                if copy_map[row][col] == BLANK or copy_map[row][col] == POSSIBLE_POINT:
                    flag = False
                    break
        # 그냥 이미 모든 가능한공간이 바이러스인것
        if flag:
            return req_time

        if not que:
            return INF

        tmp_que = deque()
        while que:
            row, col = que.popleft()

            for d in range(0, 4):
                next_row = row + dr[d]
                next_col = col + dc[d]
                
                if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                    continue
                if copy_map[next_row][next_col] == WALL or copy_map[next_row][next_col] == VIRUS:
                    continue
                if visited[next_row][next_col]:
                    continue
                visited[next_row][next_col] = True
                copy_map[next_row][next_col] = VIRUS
                tmp_que.append((next_row, next_col))

        while tmp_que:
            row, col = tmp_que.popleft()
            que.append((row, col))
        req_time += 1



def comb(arr, visited, start, n, r, m, lab_map):
    global answer
    if r == 0:
        start_arr = [0] * m
        idx = 0
        for i in range(0, n):
            if visited[i]:
                start_arr[idx] = arr[i]
                idx += 1
        res = bfs(start_arr, lab_map)
        answer = min(res, answer)
        return
    for i in range(start, n):
        if visited[i]:
            continue
        visited[i] = True
        comb(arr, visited, i+1, n, r-1, m, lab_map)
        visited[i] = False


INF = 9876543211
VIRUS = -1
BLANK = 0
WALL = 1
POSSIBLE_POINT = 2

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))

pos_arr = []
for row in range(0, N):
    for col in range(0, N):
        if MAP[row][col] == POSSIBLE_POINT:
            pos_arr.append((row, col))
check_arr = [False] * (len(pos_arr))
answer = INF
comb(pos_arr, check_arr, 0, len(pos_arr), M, M, MAP)

if answer == INF:
    answer = -1
print(answer)