from collections import deque


def bfs(start_row, start_col, end_row, end_col):
    
    visited = [[False] * N for _ in range(0, N)]
    
    dr = [-2, -2, 0, 0, 2, 2]    
    dc = [-1, 1, -2, 2, -1, 1]    
    
    que = deque()
    visited[start_row][start_col] = True
    que.append((start_row, start_col, 0))
    
    while que:
        
        row, col, cnt = que.popleft()
        if row == end_row and col == end_col:
            return cnt
    
        for d in range(0, 6):
            next_row = row + dr[d]
            next_col = col + dc[d]
    
            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= N:
                continue
            if visited[next_row][next_col]:
                continue
            visited[next_row][next_col] = True
            que.append((next_row, next_col, cnt+1))
    return -1
            
N = int(input())
r1, c1, r2, c2 = map(int, input().split())

answer = bfs(r1, c1, r2, c2)

print(answer)