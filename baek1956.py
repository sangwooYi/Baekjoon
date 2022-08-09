import sys
sys.stdin = open("baek1956.txt")




V, E = map(int, input().split())

INF = 987654321
DP = [[INF] * (V+1) for _ in range(0, V+1)]
for i in range(0, E):
    a, b, c = map(int, input().split())
    DP[a][b] = c

# 고의적으로 사이클을 만든다.
for i in range(1, V+1):
    for s in range(1, V+1):
        for e in range(1, V+1):
            DP[s][e] = min(DP[s][e], DP[s][i] + DP[i][e])


answer = INF
for i in range(1, V+1):
    answer = min(answer, DP[i][i])
if answer == INF:
    print(-1)
else:
    print(answer)