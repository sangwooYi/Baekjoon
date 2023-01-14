import sys
sys.stdin = open("baek2194.txt")
from collections import deque


"""
왼쪽 이동시에는 top_row, left_col ~ bottom_row, left_col 까지
오른쪽이동시에는  top_row, right_col, bottom_row, right_col 까지
위로 이동시에는 top_row, left_col ~ top_row, right_col 까지
아래 이동시에는 bottom_row, left_col ~ bottom_row, right_col 까지 장애물 체크
"""


def is_over_by_left_top(top_row, left_col):

    bottom_row = top_row+(A-1)
    right_col = left_col+(B-1)
    
    if top_row < 0 or left_col < 0 or bottom_row >= N or right_col >= M:
        return True
    return False


def is_movable(top_row, left_col, oper):

    up = 0
    down = 1
    left = 2
    right = 3

    bottom_row = top_row + (A-1)
    right_col = left_col + (B-1)

    flag = True
    if oper == up:
        for i in range(0, B):
            if MAP[top_row][left_col+i]:
                flag = False
                break
    elif oper == down:
        for i in range(0, B):
            if MAP[bottom_row][left_col+i]:
                flag = False
                break
    elif oper == left:
        for i in range(0, A):
            if MAP[top_row+i][left_col]:
                flag = False
                break
    elif oper == right:
        for i in range(0, A):
            if MAP[top_row+i][right_col]:
                flag = False
                break
    return flag

def find_min_path(start_point, end_point):
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    que = deque()


    visited = [[False] * M for _ in range(0, N)]
    visited[start_point[0]][start_point[1]] = True
    que.append((start_point[0], start_point[1], 0))

    while que:
        row, col, path = que.popleft()

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            # 범위를 벗어나는지 체크
            if is_over_by_left_top(next_row, next_col):
                continue
            # 이동 가능한지 체크 
            if not is_movable(next_row, next_col, d):
                continue
            if next_row == end_point[0] and next_col == end_point[1]:
                return path+1
            if visited[next_row][next_col]:
                continue
            visited[next_row][next_col] = True
            que.append((next_row, next_col, path+1))
    return -1

N, M, A, B, K = map(int, input().split())
MAP = [[0] * M for _ in range(0, N)]

for i in range(0, K):
    r, c = map(int, input().split())
    MAP[r-1][c-1] = 1
start_point = list(map(int, input().split()))
end_point = list(map(int, input().split()))


# 인덱스와 번호 동기화
start_point[0] -= 1
start_point[1] -= 1
end_point[0] -= 1
end_point[1] -= 1

answer = find_min_path(start_point, end_point)
print(answer)