import sys
sys.stdin = open("baek1719.txt")


INF = 987654321
N, M = map(int, input().split())
DP = [[INF] * (N+1) for _ in range(0, N+1)]
answer = [[0] * (N+1) for _ in range(0, N+1)]
for i in range(0, M):
    # a, b 노드 // c는 cost
    a, b, c = map(int, input().split())
    DP[a][b] = c
    DP[b][a] = c

for s in range(1, N+1):
    for e in range(1, N+1):
        if s != e:
            answer[s][e] = e

# 플로이드 와샬
# 총 N번 (노드 갯수만큼) 반복하며 매 반복마다 시작점 - 도착점을
# 각각 1 부터 ~ N 노드까지 반복해서 비교한다.
# DP[s][e] = min(DP[s][e], DP[s][i] + DP[i][e])
# 즉 현재까지 s -> e 로가는 최솟값 vs i를 거쳐 e로 도착하는 경로중 최솟값을 찾는 것
for i in range(1, N+1):
    for s in range(1, N+1):
        for e in range(1, N+1):
            if s == e:
                answer[s][e] = "-"
            else:
                if DP[s][e] > DP[s][i] + DP[i][e]:
                    DP[s][e] = DP[s][i] + DP[i][e]
                    # 가장 먼저 들러야 하는 경로를 저장해야하므로 이렇게 갱신해야함!
                    answer[s][e] = answer[s][i]

for i in range(1, N+1):
    for j in range(1, N+1):
        if j == N:
            print(answer[i][j])
        else:
            print(answer[i][j], end=" ")