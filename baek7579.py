import sys
sys.stdin = open("baek7579.txt")

"""
목표는 재활성화시 필요한 비용이 최소가 되도록 하면서 M바이트 '이상' 메모리를 확보하는 것

N의 범위가 100까지밖에 안된다.

메모리는 천만까지범위, 비용은 최대 100*100 1만임 따라서 
DP[i][j] 에서 j를 메모리가 아니라, 비용으로 가고 DP에는 저장된 메모리값이 저장됨
=> DP[i][j] 탐색해서 저장된 값이 M 이상인 애들중에 j의 최솟값을 찾으면 됨

전형적인 배낭문제!
가능한 최소비용으로 M 이상의 메모리를 확보하여야 하므로
DP[i][j]는 i번쨰까지 체크하여 j 비용으로 확보할수 잇는 '최대 메모리가' 되는것
그 DP 값에서 M 이상인 애들 중에 j가 가장 작은 값을 답으로 출력해 주면 됨!


"""

N, M = map(int, input().split())
# 차지하는 메모리
memories = list(map(int, input().split()))
# 재활성화시 필요한 비용
costs = list(map(int, input().split()))
total_cost = 0
for i in range(0, N):
    total_cost += costs[i]

DP = [[0] * (total_cost+1) for _ in range(0, N)]

answer = total_cost
for i in range(0, N):
    memory = memories[i]
    cost = costs[i]
    for j in range(1, total_cost+1):
        if j < cost:
            # 넣을수 없으면 무조건 이 체크
            DP[i][j] = DP[i-1][j]
        else:
        # 이게 배낭문제!
                    #현재 i번을 안쓰는것,  #현재 i번을 쓰는것
            DP[i][j] = max(DP[i-1][j], DP[i-1][j-cost]+memory)
        # 문제 잘 읽자. M바이트 이상이기만하면 상관 없음.. (따라서 배낭 문제를 어떻게 풀어야하는지 나오는것)
        if DP[i][j] >= M:
            if answer > j:
                answer = j
print(answer)