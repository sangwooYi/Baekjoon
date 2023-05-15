import sys
sys.stdin = open("baek2167.txt")


N, M = map(int, input().split())
MAP = [0]*N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))

accum_map = [[0] * M for _ in range(0, N)]
# 누적합 구현 (한쪽방향 누적합 구한 후, 다른 방향으로 한번 더 누적합)
for row in range(0, N):
    for col in range(0, M):
        if col == 0:
            accum_map[row][0] = MAP[row][0]
        else:
            accum_map[row][col] = accum_map[row][col-1]+MAP[row][col]
for col in range(0, M):
    for row in range(1, N):
        accum_map[row][col] += accum_map[row-1][col]


K = int(input())
# map[a][b] ~ map[c][d] 까지 누적합 (a<=c && b<=d) => map[c][d]-map[c-1][b-1]-map[a-1][d-1]+map[c-1][b-1]
for i in range(0, K):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    ans = 0
    ans += accum_map[c][d]
    if a > 0:
        ans -= accum_map[a-1][d]
    if b > 0:
        ans -= accum_map[c][b-1]
    if a > 0 and b > 0:
        ans += accum_map[a-1][b-1]      
    print(ans)
