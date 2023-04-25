import sys
from collections import deque
sys.stdin = open("baek21922.txt")


"""
1번은 좌/우 방향 바람은 반대로 상/하는 그대로
2번은 상/하 방향은 반대로, 좌/우는 그대로
3번은 상<>우 // 하<>좌 로 바꾼다
4번은 하<>우 // 상<>좌 로 바꾼다

방향은 0상 1우 2하 3좌 로 간다.
visited 배열은 [r][c][d] 로 구성 (최대 8백만)

=> 이건 자바로는 OK 근데 파이썬으로는 시간초과 (..)
따라서 차라리 그냥 각 바람이 끝날때까지 보내보자
50 * 4이므로 => 이게 차라리 통과가 된다..
"""

# 자바는 이것도 된다.. 근데 파이썬은 안된다 ㅠㅠ
def check_area():

    # 상우하좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    up = 0
    right = 1
    down = 2
    left = 3

    que = deque()
    visited = [[[False] * 4 for _ in range(0, M)] for _ in range(0, N)]
    for r in range(0, N):
        for c in range(0, M):
            if MAP[r][c] == 9:
                for d in range(0, 4):
                    visited[r][c][d] = True
                    que.append((r, c, d))

    while que:

        row, col, dir = que.popleft()
        next_dir = dir 
        # 좌우가 막힌다.
        if MAP[row][col] == 1:
            # 1<->3
            if dir == left or dir == right:
                next_dir = (dir+2)%4
        # 상하가 막힌다.
        if MAP[row][col] == 2:
            # 0<->2
            if dir == up or dir == down:
                next_dir = (dir+2)%4

        # 상 <-> 우 // 하 <-> 좌 로 바뀜
        if MAP[row][col] == 3:
            if dir == 0:
                next_dir = 1
            if dir == 1:
                next_dir = 0
            if dir == 3:
                next_dir = 2
            if dir == 2:
                next_dir = 3
        # 상 <-> 좌 // 하 <-> 우 로 바뀜
        if MAP[row][col] == 4:
            if dir == 0:
                next_dir = 3
            if dir == 3:
                next_dir = 0
            if dir == 2:
                next_dir = 1
            if dir == 1:
                next_dir = 2     

        next_row = row + dr[next_dir]
        next_col = col + dc[next_dir]

        if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
            continue
        if visited[next_row][next_col][next_dir]:
            continue
        visited[next_row][next_col][next_dir] = True
        que.append((next_row, next_col, next_dir))

    cool_area = 0
    for r in range(0, N):
        for c in range(0, M):
            flag = False
            for d in range(0, 4):
                if visited[r][c][d]:
                    flag = True
                    break
            if flag:
                cool_area += 1
    return cool_area


# 오히려 선풍기 바람을 기준으로 bfs 진행하는게 더 효율적인 문제!
# 진짜 입력 괴랄한게 아닌이상 파이썬으로도 풀수있다.. 집중하자
def bfs():
    # 상우하좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    up = 0
    right = 1
    down = 2
    left = 3
    que = deque()

    # 2차원으로 진행
    visited = [[False] * M for _ in range(0, N)]
    for r in range(0, N):
        for c in range(0, M):
            if MAP[r][c] == 9:
                que.append((r, c))
                visited[r][c] = True

    while que:
        row, col = que.popleft()

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]
            
            dir = d
            while 0 <= next_row < N and 0 <= next_col < M:
                visited[next_row][next_col] = True

                if MAP[next_row][next_col] == 9:
                    break
                # 좌/우는 종료
                if MAP[next_row][next_col] == 1:
                    if dir == left or dir == right:
                        break
                # 상/하는 종료
                if MAP[next_row][next_col] == 2:
                    if dir == up or dir == down:
                        break
                # 상 <-> 우 // 하 <-> 좌 로 바뀜    
                if MAP[next_row][next_col] == 3:
                    if dir == up:
                        next_dir = right
                    if dir == right:
                        next_dir = up
                    if dir == down:
                        next_dir = left
                    if dir == left:
                        next_dir = down
                    dir = next_dir
                # 상 <-> 좌 // 하 <-> 우 로 바뀜    
                if MAP[next_row][next_col] == 4:
                    if dir == up:
                        next_dir = left
                    if dir == left:
                        next_dir = up
                    if dir == down:
                        next_dir = right
                    if dir == right:
                        next_dir = down
                    dir = next_dir
                next_row += dr[dir]
                next_col += dc[dir]
    
    area = 0
    for r in range(0, N):
        for c in range(0, M):
            if visited[r][c]:
                area += 1
    return area
                
N, M = map(int, sys.stdin.readline().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, sys.stdin.readline().split()))


answer = bfs()
print(answer)