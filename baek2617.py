import sys
sys.stdin = open("baek2617.txt")

"""
그냥 
1. 본인보다 큰 경로만 나타내는 애
2. 본인보다 작은 경로만 나타내는 애
각각 선언한 후, 
플로이드 와샬 돌리고,
간선이 존재하는 갯수를 파악하면 끝!
N이 최대 99이므로 충분히 가능한 로직!

"""

N, M = map(int, input().split())
INF = 987654321
BOX = [[INF] * (N+1) for _ in range(0, N+1)]
BOX2 = [[INF] * (N+1) for _ in range(0, N+1)]
for i in range(0, M):
    # a 무게 > b 무게, 일방향성임!
    a, b = map(int, input().split())
    # 큰 방향
    BOX[a][b] = 1
    # 작은 방향
    BOX2[b][a] = 1

for i in range(1, N+1):
    for s in range(1, N+1):
        for e in range(1, N+1):
            if s == e:
                BOX[s][e] = 0
                BOX2[s][e] = 0
            else:
                BOX[s][e] = min(BOX[s][e], BOX[s][i] + BOX[i][e])
                BOX2[s][e] = min(BOX2[s][e], BOX2[s][i] + BOX2[i][e])

cnt = 0
for i in range(1, N+1):
    tmp = 0
    tmp2 = 0
    for j in range(1, N+1):
        if i == j:
            continue
        if BOX[i][j] != INF:
            tmp += 1
        if BOX2[i][j] != INF:
            tmp2 += 1
    if tmp >= (N+1)//2:
        cnt += 1
    if tmp2 >= (N+1)//2:
        cnt += 1
print(cnt)