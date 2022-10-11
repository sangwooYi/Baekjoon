import sys
from collections import deque
sys.stdin = open("baek1726.txt")


"""
기본적으로 해당 

맵 사이즈가 최대 100*100이라 만만하다.
"""

def is_outbound(row, col, r, c):
    if row < 0 or col < 0 or row >= r or col >= c:
        return True
    return False

def is_target(now, target):
    if now == target:
        return True
    return False


def calc_min_path(game_map, start, target):
    if start == target:
        return 0
    r = len(game_map)
    c = len(game_map[0])
    que = deque()
    # 동 남 서 북 
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    # visited[a][b][c]  a, b 좌표에서 c 방향으로 방문한 이력을 체크하는 것
    visited = [[[False for _ in range(0, 4)] for _ in range(0, c)] for _ in range(0, r)]
    start_row, start_col, start_dir = start

    visited[start_row][start_col][start_dir] = True

    # 행, 열, 방향, path 를 계속 체크
    que.append((start_row, start_col, start_dir, 0))

    while que:
        row, col, direct, path = que.popleft()
        # 1부터 3까지, 이동가능 여부는 여기서만 체크한다
        for k in range(1, 4):
            next_row = row + dr[direct]*k
            next_col = col + dc[direct]*k

            # 1 ~ 3까지 기다리지 말고, 중간에 이동안되는 칸이나오면 즉시 종료, 더 멀리 갈 필요가 없음
            if is_outbound(next_row, next_col, r, c):
                break
            # 이동 불가
            if game_map[next_row][next_col] == 1:
                break
            if visited[next_row][next_col][direct]:
                continue
            if next_row == target[0] and next_col == target[1]:
                if is_target((next_row, next_col, direct), target):
                    return path+1
            visited[next_row][next_col][direct] = True
            que.append((next_row, next_col, direct, path+1))
        # 방향 전환 (-1, 1만 체크하면 됨)
        for d in range(-1, 2, 2): 
            next_direct = direct + d
            # -1 된순간 3으로 바꾸어주고
            if next_direct < 0:
                next_direct = 3
            # 4가 된순간 0으로 바꾸어줌, 방향을 한번에 90도만 회전하는 문제라서 가능한 로직
            elif next_direct > 3:
                next_direct = 0
            if visited[row][col][next_direct]:
                continue
            if row == target[0] and col == target[1]:
                if is_target((row, col, next_direct), target):
                    return path+1
            visited[row][col][next_direct] = True
            que.append((row, col, next_direct, path+1))


N, M = map(int, input().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))

# 동 0 남 1 서 2 북 3 으로 컨버팅
# 문제에서는 동 1  서 2  남 3 북 4
conv_delta = { 1: 0,  2: 2,  3: 1, 4: 3}
# r/c 도 인덱스는 0부터, 델타함수도 0부터 시작이나
# 주어진 input값은 모두 1부터 시작
a, b, s = list(map(int, input().split()))
start_state = (a-1, b-1, conv_delta[s])
a, b, s = list(map(int, input().split()))
target_state = (a-1, b-1, conv_delta[s])

answer = calc_min_path(MAP, start_state, target_state)
print(answer)