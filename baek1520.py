import sys
sys.stdin = open("baek1520.txt")

"""
아이디어!

500 * 500 이므로 DFS로는 택도 없다.
20*20 이하면, DFS로도 비벼볼수 있을듯?

Idea1.
DP[방향][row][col] 요걸로 도전?

최악의 경우 약 ≒ 500*500*4  10만번 연산
"""



# 여기선 row(세로)가 M col(가로)이 N  
M, N = map(int, input().split())
MAP = [0] * M
for i in range(0, M):
    MAP[i] = list(map(int, input().split()))

# 상 좌 하 우, 해당 칸에 들어온 방향을 나타냄
DP = [[[0] * N for _ in range(0, M)] for _ in range(0, 4)]

# 상 좌 하 우 반전시 (dir+2) % 4 로 하기 위함
dr = [-1, 0, 1, 0] 
dc = [0, -1, 0, 1]
# 초깃값 세팅
for i in range(0, 4):
    DP[i][0][0] = 1

for row in range(0, M):
    for col in range(0, N):
        for i in range(0, 4):
            next_row = row + dr[i]
            next_col = col + dc[i]
            if next_row < 0 or next_col < 0 or next_row >= M or next_col >= N:
                continue
            # 본인 높이 이하인 경우는 이동 불가
            if MAP[next_row][next_col] <= MAP[row][col]:
                continue
            # 이때는 이동 가능
            direction = (i + 2) % 4
            DP[direction][row][col] += DP[direction][next_row][next_col]

ans = 0
for i in range(0, 4):
    ans += DP[i][M-1][N-1]
print(ans)
