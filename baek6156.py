import sys
sys.stdin = open("baek6156.txt")


"""
플로이드와샬 *2 를통해
나보다 순위 높은 cow 체크
나보다 순위 낮은 cow 체크

순회 후,
나보다 순위 높은 cow + 순위 낮은 cow가 N-1인 갯수 체크
"""

N, M = map(int, input().split())
INF = 987654321
# stronger_cows[a][b]  b가 a 보다 강함
stronger_cows = [[INF]*(N+1) for _ in range(0, N+1)]
# weaker_cows[a][b] b가 a 보다 약함
weaker_cows = [[INF]*(N+1) for _ in range(0, N+1)]

for i in range(0, M):
    # a > b 
    a, b = map(int, input().split())
    stronger_cows[b][a] = 1
    weaker_cows[a][b] = 1

for t in range(1, N+1):
    for s in range(1, N+1):
        for e in range(1, N+1):
            if s == e:
                stronger_cows[s][e] = 0
                weaker_cows[s][e] = 0
            else:
                stronger_cows[s][e] = min(stronger_cows[s][e], stronger_cows[s][t] + stronger_cows[t][e])
                weaker_cows[s][e] = min(weaker_cows[s][e], weaker_cows[s][t] + weaker_cows[t][e])

ans = 0
for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if i == j:
            continue
        if stronger_cows[i][j] != INF or weaker_cows[i][j] != INF:
            cnt += 1
    if cnt == N-1:
        ans += 1
print(ans)