import sys
sys.stdin = open("baek4811.txt")

"""
무조건 시작은 W (어쨌건 온전한 한조각을 받은거니까)
마지막 날은 무조건 H 
즉 경우의수는 둘째날 ~ N-1번쨰날까지만 체크하면 된다.
결국 N번 쪼개야 하므로

아이디어1.
DP[a][b]  => a번째날, b번 알약을 쪼갰을때의 경우의 수
안쪼개고 현재 있는 반쪼가리 먹거나, 새로 쪼개서 반쪽먹고 다시 넣거나
즉 DP[a][b] = DP[a-1][b] + DP[a-1][b-1]
"""

# while True:
#     N = int(input())
#     # 종료 조건
#     if N == 0:
#         break
#     DP = [[0] * (N+1) for _ in range(0, 2*N+1)]
#     # 초깃값, 처음에 시작은 무조건 쪼개야 함
#     DP[1][1] = 1
#     for i in range(2, 2*N+1):
#         # 쪼갤수 있는 횟수는 1회 ~ (날짜 // 2)회 까지임
#         for j in range(1, i//2+1):
#             DP[i][j] = DP[i-1][j] + DP[i-1][j-1]
#     # 이 풀이는 맞다고는 하는데 좀 이상하다 ㅡㅡ
#     answer = (DP[2*N][N-1] + DP[2*N][N]) 
#     print(answer)


# 여기서는 DP[i][j] 반개를 i번 한개를 j번 먹는 경우임
# 핵심은 결국 그냥 쪼개는 
while True:
    N = int(input())
    if N == 0:
        break
    DP = [[0] * (N+1) for _ in range(0, N+1)]
    # 초깃값 세팅, N일동안 계속 1개씩만 꺼내는 경우
    for i in range(1, N+1):
        DP[0][i] = 1
    for i in range(1, N+1):
        # 반개 먹는양은 j개먹는 양보다 많을 수 가없다. (i <= j)
        for j in range(i, N+1):
            # 반쪼가리 먹거나, 한개짜리를 꺼내는 경우의 합이 DP[i][j] 가 됨
            DP[i][j] = DP[i-1][j] + DP[i][j-1]
    print(DP[N][N])
