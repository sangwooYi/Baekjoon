import sys
sys.stdin = open("baek1495.txt")

"""
i 번째 노래를 연주하기 위해서는
P + V[i] 혹은 P - V[i] 로 볼륨을 변경해야하고,
볼륨은 0 이상, M 이하여야한다.
이 범위를 벗어나면 다음 곡 연주가 불가능 (-1 반환)

핵심 아이디어.
i 번째 노래 기준, 현재 음량이 j 일때
j - V[i]  ~ j + V[i] 까지중 가능한 볼륨 가능여부를 전부 체크

"""
# 0번부터 N-1번까지로 진행
N, S, M = map(int, input().split())
V = list(map(int, input().split()))
# 다이나믹 프로그래밍은 어떤 구조로 동적계획을 할지 짜는것 자체가 가장 중요
# DP[n][v]  n번째곡을 v 음량으로 연주가 가능한지 여부를 체크
DP = [[False] * (M+1) for _ in range(0, N+1)]
DP[0][S] = True

# 이렇게 1번부터 N 번까지 순차적으로 진행한다.
for i in range(1, N+1):
    # 각 음악 마다 0 부터 M까지 볼륨중 가능한 볼륨을 전부 체크
    # M 이 1000까지이고, N 은 50까지, 그리고 각 음악마다 최대 2가지씩 경우가 나오기 때문에
    # 풀이가 가능했던 문제!
    for j in range(0, M+1):
        if not DP[i-1][j]:
            continue
        # 만약 i-1번째곡에서 j음량으로 연주가 가능하다면
        # 각 경우당 2가지씩으로 분기가 됨 (j - V[i-1] 로 할지  j + V[i-1]로 할지)
        # 두 경우 각각 가능한 경우면 전부 체크
        if (j - V[i-1]) >= 0:
            DP[i][j-V[i-1]] = True
        if (j + V[i-1]) <= M:
            DP[i][j+V[i-1]] = True
result = -1
for i in range(M, -1, -1):
    if DP[N][i]:
        result = i
        break
print(result) 