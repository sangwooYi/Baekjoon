import sys
sys.stdin = open("baek2662.txt")

"""
배낭 문제!
+ 경로까지 출력할 수 있어야 한다.
단순 배낭문제의 응용!
충분히 풀 수 있어야 함
다시 풀어 볼 것!
"""


N, M = map(int, input().split())
# invest[i][j] i 번째 기업에게 j 원을 투자할떄 이익을 저장 
invest = [[0] * (N+1) for _ in range(0, M+1)]
for i in range(0, N):
    temp = list(map(int, input().split()))
    for j in range(1, len(temp)):
        invest[j][i+1] = temp[j]


# DP[i] i원을 투자할떄까지의 최대 이익
DP = [0] * (N+1)
# 경로를 출력해야함 (경로 출력 필요없으면 내 풀이도 가능했음)
path = [[] for _ in range(0, N+1)]

# 첫번째 기업은 그냥 진행 (초깃값 개념)
for i in range(0, N+1):
    DP[i] = invest[1][i]
    path[i].append(i)

# 두번쨰 기업부터 진행
for i in range(2, M+1):
    for j in range(N, -1, -1):
        add = 0
        for k in range(1, j+1):
            if DP[j-k] + invest[i][k] > DP[j]:
                DP[j] = DP[j-k] + invest[i][k]
                path[j] = []
                # 리스트 deep copy 해줘야 함. 
                for l in range(0, len(path[j-k])):
                    path[j].append(path[j-k][l])
                add = k
        path[j].append(add)
print(DP[N])
print(" ".join(map(str, path[N])))