import sys
sys.stdin = open("baek2458.txt")

"""
자기보다 큰쪽을 체크하는 단방향 이차원 리스트,
자기보다 작은쪽을 체크하는 단방향 이차원 리스트
각각을 플로이드 와샬을 돌린후,
각 노드마다 upper/lower 리스트를 전부 순회하며 INF 아닌 값이 N-1 만큼 존재하는 갯수를 구함
"""

N, M = map(int, input().split())
INF = 987654321
# 자기보다 큰 방향을 체크
upper = [[INF] * (N+1) for _ in range(0, N+1)]
# 자기보다 작은 방향을 체크
lower = [[INF] * (N+1) for _ in range(0, N+1)]
for i in range(0, M):
    a, b = map(int, input().split())
    upper[a][b] = 1
    lower[b][a] = 1

# O(N**3) 따라서 최대 노드 1000까지임  
for i in range(1, N+1):
    for s in range(1, N+1):
        for e in range(1, N+1):
            if s == e:
                upper[s][e] = 0
                lower[s][e] = 0
            else:
                upper[s][e] = min(upper[s][e], upper[s][i] + upper[i][e])
                lower[s][e] = min(lower[s][e], lower[s][i] + lower[i][e])

answer = 0
for i in range(1, N+1):
    cnt = 0
    for j in range(1, N+1):
        if i != j:
            if lower[i][j] != INF:
                cnt += 1
            if upper[i][j] != INF:
                cnt += 1
    if cnt == N-1:
        answer += 1
print(answer)
