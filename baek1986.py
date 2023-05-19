import sys
sys.stdin = open("baek1986.txt")

N, M = map(int, sys.stdin.readline().split())
Q = list(map(int, sys.stdin.readline().split()))
K = list(map(int, sys.stdin.readline().split()))
P = list(map(int, sys.stdin.readline().split()))

Q_cnt = Q[0]
K_cnt = K[0]
P_cnt = P[0]
Q_stack = [0] * Q_cnt
K_stack = [0] * K_cnt
P_stack = [0] * P_cnt


MAP = [[0] * M for _ in range(0, N)]

# 상 하 좌 우 좌상 우상 우하 좌하 총 8방향, 퀸용
dr_q = [-1 ,1, 0, 0, -1, -1, 1, 1]
dc_q = [0, 0, -1, 1, -1, 1, 1, -1]

# 8방향 킹 용
dr_k = [-1, -2, -2, -1, 1, 2, 2, 1]
dc_k = [-2, -1, 1, 2, 2, 1, -1, -2]

# 장애물은 2로, 그냥 단순 가능 경로는 1로 표기
for i in range(1, 2*Q_cnt+1, 2):
    idx = i//2
    Q_stack[idx] = (Q[i]-1, Q[i+1]-1)
    MAP[Q[i]-1][Q[i+1]-1] = 2

for i in range(1, 2*K_cnt+1, 2):
    idx = i//2
    K_stack[idx] = (K[i]-1, K[i+1]-1)
    MAP[K[i]-1][K[i+1]-1] = 2
for i in range(1, 2*P_cnt+1, 2):
    idx = i//2
    P_stack[idx] = (P[i]-1, P[i+1]-1)   
    MAP[P[i]-1][P[i+1]-1] = 2

# 퀸과 킹 이동 가능 위치 체크
for i in range(0, Q_cnt):
    row, col = Q_stack[i]
    # 장애물 나올때까지 or 맵 끝날때까지 상하좌우대각선 이동
    for d in range(0, 8):
        term = 1
        while True:
            next_row = row + dr_q[d]*term
            next_col = col + dc_q[d]*term

            # 맵 밖이면 종료
            if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
                break
            # 장애물이면 종료
            if MAP[next_row][next_col] == 2:
                break
            MAP[next_row][next_col] = 1
            term += 1
for i in range(0, K_cnt):
    row , col = K_stack[i]
    # 그냥 8방향 이동
    for d in range(0, 8):
        next_row = row + dr_k[d]
        next_col = col + dc_k[d]
        if next_row < 0 or next_col < 0 or next_row >= N or next_col >= M:
            continue
        if MAP[next_row][next_col] == 2:
            continue
        MAP[next_row][next_col] = 1

answer = 0
for r in range(0, N):
    for c in range(0, M):
        if MAP[r][c] == 0:
            answer += 1
print(answer)