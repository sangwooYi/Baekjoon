import sys
sys.stdin = open("baek11404.txt")

"""
플로이드 와샬 알고리즘 공부!
vs 다익스트라 (얘는 A노드 => B노드 (음수값 X))
=> 음수값이 있는 경우는 벨만 포드 알고리즘!
플로이드 와샬. 모든 간선끼리의 최솟값을 한번에 구함
(O(N**2)이기에, 노드가 많아지면 이 알고리즘은 힘들다)

+ 플로이드 와샬은 애초에 인접행렬로 구성하는게 효율적!
플로이드 와샬의 핵심은
'거쳐가는 노드'가 어떤건지를, 모든 노드에 대해 전부 따져본다는 것
"""


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
INF = 987654321
DP = [[INF] * (N+1) for _ in range(0, N+1)]


for i in range(0, M):
    a, b, c = map(int, sys.stdin.readline().split())
    # 한 간선에대해 여러 값이 들어올 수 있다.
    DP[a][b] = min(DP[a][b], c)

for i in range(1, N+1):
    for s in range(1, N+1):
        for e in range(1, N+1):
            if s == e:
                DP[s][e] = 0
            else:
                # 현재 저장된 값 vs i 노드를 거쳐서 e로 도착한 거리중 최솟값
                DP[s][e] = min(DP[s][e], DP[s][i] + DP[i][e])

for i in range(1, N+1):
    for j in range(1, N+1):
        if DP[i][j] == INF:
            ans = 0
        else:
            ans = DP[i][j]
        if j == N:
            print(ans)
        else:
            print(ans, end=" ")