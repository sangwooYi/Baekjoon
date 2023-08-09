import sys
sys.setrecursionlimit(10**5)
sys.stdin = open("baek1189.txt")


"""
출발은 R-1, 0
도착은 0, C-1
"""

def dfs(row, col, path):
    global cnt

    if row == 0 and col == C-1:
        if path == K:
            cnt += 1
            return
    # 경로가 K 이상이 되었는데 목적지가 아니면 종료
    if path >= K:
        return
    for d in range(0, 4):
        next_row = row + dr[d]
        next_col = col + dc[d]

        if next_row < 0 or next_col < 0 or next_row >= R or next_col >= C:
            continue
        if visited[next_row][next_col]:
            continue
        if MAP[next_row][next_col] == "T":
            continue
        visited[next_row][next_col] = True
        dfs(next_row, next_col, path+1)
        visited[next_row][next_col] = False
        

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C, K = map(int, input().split())
MAP = [0] * R
for i in range(0, R):
    MAP[i] = list(input())

cnt = 0
visited = [[False] * C for _ in range(0, R)]
visited[R-1][0] = True
dfs(R-1, 0, 1)
print(cnt)