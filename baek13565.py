import sys
from collections import deque
sys.stdin = open("baek13565.txt")



def bfs(start_row, start_col):

    que = deque()
    que.append((start_row, start_col))


    while que:
        row, col = que.popleft()

        if row == R-1:
            return True

        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= R or next_col >= C:
                continue
            if MAP[next_row][next_col]:
                continue
            if visited[next_row][next_col]:
                continue
            visited[next_row][next_col] = True
            que.append((next_row, next_col))
    return False

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, sys.stdin.readline().split())
MAP = [0] * R
for i in range(0, R):
    MAP[i] = list(map(int, sys.stdin.readline().rstrip()))


visited = [[False] * C for _ in range(0, R)]

flag = False

for i in range(0, C):
    # 한 번이라도 끝까지 갔으면 종료
    if flag:
        break
    # 이미 방문 or 검은격자면 pass
    if visited[0][i]:
        continue
    if MAP[0][i]:
        continue
    visited[0][i] = True
    res = bfs(0, i)
    if res:
        flag = res

if flag:
    print("YES")
else:
    print("NO")