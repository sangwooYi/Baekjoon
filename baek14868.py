import sys
sys.setrecursionlimit(10**5)
from collections import deque  # .append(), .popleft() 만 쓸 줄 알면 됨
sys.stdin = open("baek14868.txt")

"""
언
"""


def find(x):
    if x == parent[x]:
        return x
    px = find(parent[x])
    parent[x] = px
    return px

def union(x, y):
    px = find(x)
    py = find(y)

    # px <= py 로 가던 이걸로가던 큰차이 X, 작은 쪽을 루트로 가져간다는게 핵심
    if px < py:
        parent[py] = px
    else:
        parent[px] = py

def bfs():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while que:
        row, col, cnt = que.popleft()
        for d in range(0, 4):
            next_row = row + dr[d]
            next_col = col + dc[d]
            
            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                continue
            if MAP[next_row][next_col] != 0:
                if find(MAP[next_row][next_col][0]) != find(MAP[row][col][0]):
                    union(MAP[row][col][0], MAP[next_row][next_col][0])
                    flag = True
                    head = find(1)
                    for i in range(2, M+1):
                        if head != find(i):
                            flag = False
                            break
                    if flag:
                        res = max(cnt, MAP[next_row][next_col][1])
                        return res

                continue
            MAP[next_row][next_col] = [MAP[row][col][0], cnt+1]
            que.append((next_row, next_col, cnt+1))    


N, M = map(int, sys.stdin.readline().split())

parent = [i for i in range(0, M+1)]
MAP = [[0] * N for _ in range(0, N)]
que = deque()
for i in range(0, M):
    x, y = map(int, sys.stdin.readline().split())
    # 값이 1부터 시작
    MAP[y-1][x-1] = [i+1, 0]
    # 위치, 햇수
    que.append((y-1, x-1, 0))

ans = bfs()
print(ans)