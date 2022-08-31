import sys
from collections import deque # .append(넣을 값), .popleft()
# 만약 내가 만든 Queue로 안풀리면 그냥 dequeue 쓰자1 조금더 빠르다.
# + 시간 빡빡한 문제일수록 가지치기를 잘 해야 함!
sys.stdin = open("baek14442.txt")

"""
기본적으로 BFS
단 벽을 만나면
=> 벽 부순횟수 K미만이면 => 벽 부수는것도 고려
=> 아니면 그냥 벽만나면 pass
"""

def bfs(arr, k):

    r = len(arr)
    c = len(arr[0])
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # visited[r][c][k] k번 벽을 부숴서 r, c, 에 도달하는 경로 체크
    visited = [[[0] * (k+1) for _ in range(0, c)] for _ in range(0, r)]
    que = deque()
    visited[0][0][0] = 1
    # 행, 열, 벽 부순횟수, 경로
    que.append((0, 0, 0, 1))

    while que:
        row, col, chance, time = que.popleft()
        # 여기서 체크해주는것이 오히려 더 효율적이다.//
        if row == r-1 and col == c-1:
            return time

        for i in range(0, 4):
            next_row = row + dr[i]
            next_col = col + dc[i]
            # 맵 밖
            if next_row < 0 or next_col < 0 or next_row >= r or next_col >= c:
                continue
            # 이미 방문한 곳일 때
            if visited[next_row][next_col][chance]:
                continue
            # 벽을 만날 떄
            if arr[next_row][next_col] == "1":
                # 아직 벽 부수는 횟수 남았을 때만 진행
                if chance < k:
                    # 이곳도 아직 방문하지 않았을떄만 (이게 시간초과난 원인중 한가지..)
                    if not visited[next_row][next_col][chance+1]:
                        visited[next_row][next_col][chance+1] = 1
                        que.append((next_row, next_col, chance+1, time+1))
                continue
            visited[next_row][next_col][chance] = 1
            que.append((next_row, next_col, chance, time+1))
    return -1

N, M, K = map(int, sys.stdin.readline().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(sys.stdin.readline().rstrip())

answer = bfs(MAP, K)
print(answer)