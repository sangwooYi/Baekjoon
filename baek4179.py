import sys
sys.stdin = open("baek4179.txt")
from collections import deque

"""
DFS 는 절대 안되고 (행, 열이 1000까지면 왠만하면 DFS는 아니다.),
BFS 응용문제!

BFS 를 한턴씩 돌려야 하는경우, 아래처럼 하면된다! 
이론을 알고있으면 충분히 응용 가능한 문제!
"""

def find_min_time():
    
    my_que = deque()
    fire_que = deque()
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visited = [[False] * C for _ in range(0, R)]
    for row in range(0, R):
        for col in range(0, C):
            if MAP[row][col] == "J":
                my_que.append((row, col))
                visited[row][col] = True
            if MAP[row][col] == "F":
                fire_que.append((row, col))
    time = 0
    while True:
        # 불먼저
        tmp_fire_que = deque()
        while fire_que:
            row, col = fire_que.popleft()

            for d in range(0, 4):
                next_row = row + dr[d]
                next_col = col + dc[d]

                if next_row < 0 or next_col < 0 or next_row >= R or next_col >= C:
                    continue
                if MAP[next_row][next_col] == "#":
                    continue
                if MAP[next_row][next_col] == "F":
                    continue
                MAP[next_row][next_col] = "F"
                tmp_fire_que.append((next_row, next_col))
        
        tmp_my_que = deque()
        while my_que:
            row, col = my_que.popleft()

            for d in range(0, 4):
                next_row = row + dr[d]
                next_col = col + dc[d]

                if next_row < 0 or next_col < 0 or next_row >= R or next_col >= C:
                    return time+1
                if MAP[next_row][next_col] == "#":
                    continue
                if MAP[next_row][next_col] == "F":
                    continue
                if visited[next_row][next_col]:
                    continue
                visited[next_row][next_col] = True
                tmp_my_que.append((next_row, next_col))
        # 더이상 갈곳이 없으면 종료
        if not tmp_my_que:
            break
        while tmp_fire_que:
            row, col = tmp_fire_que.popleft()
            fire_que.append((row, col))
        while tmp_my_que:
            row, col = tmp_my_que.popleft()
            my_que.append((row, col))
        time += 1
    return "IMPOSSIBLE"



R, C = map(int, input().split())
MAP = [0] * R
for i in range(0, R):
    MAP[i] = list(input())

answer = find_min_time()
print(answer)
