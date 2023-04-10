from collections import deque

def bfs(s_row, s_col, e_row, e_col, n):

    que = deque()
    visited = [[False] * n for _ in range(0, n)]

    visited[s_row][s_col] = True
    que.append((s_row, s_col, 0))

    while que:

        row, col, cnt = que.popleft()
        
        if row == e_row and col == e_col:
            return cnt
        
        for d in range(0, 8):
            next_row = row + dr[d]
            next_col = col + dc[d]

            if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n:
                continue
            if visited[next_row][next_col]:
                continue
            visited[next_row][next_col] = True
            que.append((next_row, next_col, cnt+1))

# 나이트 이동 경우
dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [-2, -1, 1, 2, 2, 1, -1, -2]

T = int(input())
for tc in range(0, T):
    I = int(input())

    start_row, start_col = map(int, input().split())
    end_row, end_col = map(int, input().split())

    answer = bfs(start_row, start_col, end_row, end_col, I)
    print(answer)
