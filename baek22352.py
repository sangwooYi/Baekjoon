import sys
from collections import deque
sys.stdin = open("baek22352.txt")


"""
아이디어
쉽게생각하자 ...
순회하다가 다른 지점 발견 => BFS 진행
그리고 BFS는 애초에 1회만 가능하다
"""

# area 세팅용

def bfs(start_row, start_col):

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    pre_color = pre_MAP[start_row][start_col]
    post_color = post_MAP[start_row][start_col]
    pre_MAP[start_row][start_col] = post_color
    que = deque()
    visited = [[False] * M for _ in range(0, N)]
    visited[start_row][start_col] = True
    que.append((start_row, start_col))

    while que:
        row, col = que.popleft()

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
                continue
            if visited[next_row][next_col]:
                continue
            if pre_MAP[next_row][next_col] != pre_color:
                continue
            pre_MAP[next_row][next_col] = post_color
            visited[next_row][next_col] = True
            que.append((next_row, next_col))


N, M = map(int, input().split())

pre_MAP = [0] * N
post_MAP = [0] * N


for i in range(0, N):
    pre_MAP[i] = list(map(int, input().split()))

for i in range(0, N):
    post_MAP[i] = list(map(int, input().split()))


flag = True
for row in range(0, N):
    if not flag:
        break
    for col in range(0, M):
        if pre_MAP[row][col] != post_MAP[row][col]:
            bfs(row, col)
            flag = False
            break

if pre_MAP == post_MAP:
    print("YES")
else:
    print("NO")