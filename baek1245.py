import sys
from collections import deque
sys.stdin = open("baek1245.txt")

"""
현재 포인트를 체크,
같은 포인트인 인접한 영역을 전부 체크 
+ 인접한 다른 높이의 영역이 한번이라도
현재 값보다 큰값이 나온다면 => flag 값 변경
flag가 True로 끝까지 유지된 경우만 +1
"""


def bfs(r, c, h):
    
    que = deque()
    que.append((r, c))
    visited[r][c] = True
    flag = True

    while que:
        row, col = que.popleft()

        for d in range(0, 8):
            next_row = row + dr[d]
            next_col = col + dc[d]
            
            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
                continue
            # pass 하는 순서를 주의하자!
            # 이미 방문하였지만, 높이체크를 위해 비교가 필요한 경우가 존재!
            if MAP[next_row][next_col] != h:
                if MAP[next_row][next_col] > h:
                    flag = False
                continue
            if visited[next_row][next_col]:
                continue
            visited[next_row][next_col] = True
            que.append((next_row, next_col))
    return flag
                    




N, M = map(int, input().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))
# 8방향임!
# 상, 상우, 우, 우하, 하, 좌하, 좌, 상좌
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


visited = [[False] * M for _ in range(0, N)]

answer = 0
for i in range(0, N):
    for j in range(0, M):
        # 이미 방문한 지점, 높이가 0인지점은 pass
        if not visited[i][j] and MAP[i][j]:
            height = MAP[i][j]
            is_peak = bfs(i, j, height)

            if is_peak:
                answer += 1
print(answer)