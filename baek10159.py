import sys
sys.stdin = open("baek10159.txt")

"""
이 문제의 경우,
O(N**3) 알고리즘으로 모든 경로를 다체크한다는 의미에서
플로이드 와샬이라는것.

근데 다른 문제와 다르게 가중치나 cost가 존재하지 않음

그냥 해당 경로가 연결 되었는지 여부만 체크하는 문제!
"""

N = int(input())
M = int(input())

INF = 987654321
dist1 = [[INF] * (N+1) for _ in range(0, N+1)]
dist2 = [[INF] * (N+1) for _ in range(0, N+1)]
for i in range(0, M):
    # 무게가 a > b 라는것 => 이건 결국 방향성 그래프와 같음! (이런걸 혼자 사고할 수 있어야 한다)
    a, b = map(int, input().split())
    # a=>b 방향으로 길이 존재 (무거운 =-> 가벼운 방향)
    dist1[a][b] = 1
    # a <= b 방향으로 길이 존재 (가벼운 => 무거운 방향)
    dist2[b][a] = 1
for i in range(1, N+1):
    for s in range(1, N+1):
        for e in range(1, N+1):
            if s == e:
                dist1[s][e] = 0
                dist2[s][e] = 0
            else:
                if dist1[s][i] != INF and dist1[i][e] != INF:
                    dist1[s][e] = 1
                if dist2[s][i] != INF and dist2[i][e] != INF:
                    dist2[s][e] = 1



for i in range(1, N+1):
    cnt = 0

    for j in range(1, N+1):
        if dist1[i][j] == INF and dist2[i][j] == INF:
            cnt += 1
    print(cnt) 