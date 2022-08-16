import sys
sys.stdin = open("baek2660.txt")

"""
전형적인
플로이드-와샬 문제
O(N**3) 알고리즘을 요구하므로
N이 아무리 커야 1000정도까지밖에 못따진다.
(대신 한번에 모든 노드끼리의 최소 경로를 찾을 수 있음)
""" 

N = int(input())
INF = 987654321
DP = [[INF] * (N+1) for _ in range(0, N+1)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    DP[a][b] = 1
    DP[b][a] = 1

for i in range(1, N+1):
    for s in range(1, N+1):
        for e in range(1, N+1):
            if s == e:
                DP[s][e] = 0
            else:
                DP[s][e] = min(DP[s][e], DP[s][i] + DP[i][e])

paths = [0] * N
for i in range(1, N+1):
    max_path = 0
    for j in range(1, N+1):
        if i != j and DP[i][j] != INF:
            max_path = max(max_path, DP[i][j])
    paths[i-1] = [max_path, i]
paths.sort()

min_path = paths[0][0]
candidates = [paths[0][1]]
for i in range(1, N):
    path = paths[i][0]
    if path == min_path:
        candidates.append(paths[i][1])
    else:
        break
candidates.sort()
print(f"{min_path} {len(candidates)}")
print(" ".join(map(str, candidates)))
