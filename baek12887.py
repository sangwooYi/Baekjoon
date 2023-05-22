import sys
sys.stdin = open("baek12887.txt")
from collections import deque


"""
첫번째 행 / 두번 째 행 모두 시행
(물론 하얀색인 경우에만)
=> 둘 각각 BFS 진행한 후, 체크된 경로 칸수+ 이미 검은색 칸수를 제외한
나머지가 바꿀 수 있는 하얀색 칸수인것 
둘중 (혹은 하나) 최댓 값을 구하면 끝
"""

def bfs(start_row, start_col):

    # 우, 하, 상 만 가능
    dr = [0, 1, -1]
    dc = [1, 0, 0]
    que = deque()
    visited = [[False] * M for _ in range(0, 2)]
    visited[start_row][start_col] = True
    # 경로 저장, 시작부터 1칸임
    que.append((start_row, start_col, 1))

    while que:
        row, col, path = que.popleft()
        # 가장 우측에 도달하면 바로 종료
        if col == M-1:
            return path

        for d in range(0, 3):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= 2 or next_col >= M:
                continue
            if visited[next_row][next_col]:
                continue
            if MAP[next_row][next_col] == "#":
                continue
            visited[next_row][next_col] = True
            que.append((next_row, next_col, path+1)) 


# 무조건 2행
M = int(input())
MAP = [0] * 2
for i in range(0, 2):
    MAP[i] = list(input())

black_cnt = 0
for row in range(0, 2):
    for col in range(0, M):
        if MAP[row][col] == "#":
            black_cnt += 1

max_ans = 0
for i in range(0, 2):
    cur_point = MAP[i][0]
    # 흰색인 경우에만 시작 가능
    if cur_point == ".":
        res = bfs(i, 0)
        cur_max = 2*M-res-black_cnt
        max_ans = max(max_ans, cur_max)

print(max_ans)