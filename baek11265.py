import sys
sys.stdin = open("baek11265.txt")


N, M = map(int, input().split())
MAP = [0] * N
for i in range(0, N):
    MAP[i] = list(map(int, input().split()))

# 플로이드-와샬 순회 순서가 중요하다! 중간에 거쳐가는 t가 가장 최상위 루프에 있어야함!
for t in range(0, N):
    for s in range(0, N):
        for e in range(0, N):
            if s == e:
                continue
            MAP[s][e] = min(MAP[s][e], MAP[s][t]+MAP[t][e])


for i in range(0, M):
    a, b, limit_time = map(int, input().split())

    req_time = MAP[a-1][b-1]
    if limit_time < req_time:
        print("Stay here")
    else:
        print("Enjoy other party")