import sys
sys.stdin = open("baek1577.txt")


# 가로, 세로 !
N, M = map(int, input().split())

ban_dict = {}
K = int(input())
for i in range(0, K):
    # col, row 순으로 좌표도 주어짐
    a, b, c, d = map(int, input().split())

    # 양방향
    ban_dict[(b, a, d, c)] = 1
    ban_dict[(d, c, b, a)] = 1

DP = [[0] * (N+1) for _ in range(0, M+1)]
# 초깃값
DP[0][0] = 1

# 변두리 먼저 진행
for r in range(1, M+1):
    chk_point = (r-1,0,r,0)
    if chk_point not in ban_dict.keys():
        DP[r][0] = DP[r-1][0]
for c in range(1, N+1):
    chk_point = (0,c-1,0, c)
    if chk_point not in ban_dict.keys():
        DP[0][c] = DP[0][c-1]

for r in range(1, M+1):
    for c in range(1, N+1):
        chk_point_x = (r, c-1, r, c)
        chk_point_y = (r-1, c, r, c)

        if chk_point_x not in ban_dict.keys():
            DP[r][c] += DP[r][c-1]
        if chk_point_y not in ban_dict.keys():
            DP[r][c] += DP[r-1][c]
print(DP[M][N])
print(DP)