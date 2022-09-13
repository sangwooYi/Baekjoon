import sys
sys.stdin = open("baek14863.txt")

"""
# DP[i][j] i구간을 j시간까지 가는데까지의 최대 모금 금액
냅색(배낭)문제임!
혼자 풀 수 있어야 한다!
"""

N, K = map(int, input().split())
walking = [0] * N
cycling = [0] * N
for i in range(0, N):
    walk_t, walk_c, cycle_t, cycle_c = map(int, input().split())
    #             시간,  금액
    walking[i] = (walk_t, walk_c)
    cycling[i] = (cycle_t, cycle_c)

# 초깃값 세팅
# DP[i][j] i구간을 j시간까지 가는데까지의 최대 모금 금액
DP = [[0] * (K+1) for _ in range(0, N+1)]
DP[1][walking[0][0]] = walking[0][1]
# 위에 walking에서 동일한 시간에서 더 많은 금액을 가져오는 input이 들어올 수도 있다. (예외처리)
DP[1][cycling[0][0]] = max(DP[1][cycling[0][0]], cycling[0][1])

# 2부터 진행, N이 최대 100까지이므로 이런식의 로직도 충분히 가능!
for i in range(2, N+1):
    walk_time, walk_cost = walking[i-1]
    cycle_time, cycle_cost = cycling[i-1]
    for j in range(0, K+1):
        # DP[i-1][j] 값이 0이라면 체크할 필요 없다. 의미없는 데이터인것
        if DP[i-1][j] == 0:
            continue
        # 각 케이스 (걷기, 자전거)를 합한 시간이 K시간을 초과하지 않을 때에만, 
        # 이전구간에서, 현재구간 걷기 // 이전구간에서 현재구간 자전거 각각 max값을 체크
        if (j+walk_time) <= K:
            DP[i][j+walk_time] = max(DP[i][j+walk_time], DP[i-1][j]+walk_cost)
        if (j+cycle_time) <= K:
            DP[i][j+cycle_time] = max(DP[i][j+cycle_time], DP[i-1][j]+cycle_cost)

answer = 0
# N번째 구간까지 도달하고 나서, K시간까지 순회하며 최댓값 찾기 (충분히 가능한 로직)
for i in range(0, K+1):
    answer = max(answer, DP[N][i])
print(answer)