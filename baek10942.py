import sys
sys.stdin = open("baek10942.txt")

"""
목표
DP[i][j]  => i ~ j 까지이가 펠린드롬인가를 체크해야 함
HOW ? 무식하게 i ~ j 까지 진짜 펠린드롬인지 전부 체크하면 나가리임.
"""

N = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

DP = [[0] * N for _ in range(0, N)]

# i가 term DP를 위해서 term을 0부터 ~ N-1 까지 진행
for i in range(0, N):
    # 시작점
    for start in range(0, N-i):
        end = start + i
        if start == end:
            DP[start][end] = 1
        # 범위의 양끝이 같다면
        elif seq[start] == seq[end]:
            # 두 글자이면 무조건 팰린드롬
            if end-start == 1:
                DP[start][end] = 1
            # 만약 start+1 ~ end-1 까지가 팰린드롬이면 start ~ end도 팰린드롬
            elif DP[start+1][end-1] == 1:
                DP[start][end] = 1
for i in range(0, M):
    a, b = map(int, sys.stdin.readline().split())
    print(DP[a-1][b-1])

# 무식한 버전
# DP = [[0] * N for _ in range(0, N)]
# for i in range(0, N):
#     # 자기 자신은 기본적으로 펠린드롬
#     DP[i][i] = 1
# for i in range(1, N):
#     for j in range(0, i):
#         term = i - j
#         flag = True
#         for k in range(0, term//2+1):
#             if seq[j+k] != seq[i-k]:
#                 flag = False
#                 break
#         if flag:
#             DP[i][j] = 1
# for i in range(0, M):
#     a, b = map(int, sys.stdin.readline().split())
#     print(DP[b-1][a-1])