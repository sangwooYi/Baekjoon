import sys
sys.setrecursionlimit(10**5)
sys.stdin = open("baek17070.txt")

"""
문제가 살짝 애매하네,,
일단 Idea1
1,1 값은 사실상 필요 X
매번 가로 / 세로 / 대각선인지 체크
가로인경우 (col+1, 가로상태 유지) or (row+1 and col+1, 대각선 상태로 업데이트) 중 가능한 경우,
세로인경우 (row+1, 세로 유지) or (row+1 and col+1 대각선으로 업데이트)
대각선인경우 (row+1 and col +1 대각선 유지) or (row + 1 , 세로로 변경) or (col+1 가로로 변경)

매번이 경우임!
BFS는 가능은 하나 시간초과 발생해버림 
visited를 안쓰는이상 BFS는 오히려 DFS에 비해 효율이 안좋은 경우도 존재!

0: 가로  1: 세로  2: 대각선

DP로도 풀수 있어야한다! (3차원 리스트 통한 메모이제이션 사용)
"""

def dfs(row, col, state):
    global ans
    if row == N-1 and col == N-1:
        ans += 1
        return
    # 대각선 이동
    if row < N-1 and col < N-1:
        if MAP[row+1][col] == 0 and MAP[row][col+1] == 0 and MAP[row+1][col+1] == 0:
            dfs(row+1, col+1, 2)

    # 가로 이동
    if state == 0 or state == 2:
        if col+1 < N and MAP[row][col+1] == 0:
            dfs(row, col+1, 0)
    # 세로 이동
    if state == 1 or state == 2:
        if row+1 < N and MAP[row+1][col] == 0:
            dfs(row+1, col, 1)

N = int(input())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))

ans = 0
dfs(0, 1, 0)
print(ans)