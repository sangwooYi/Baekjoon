import sys
from collections import deque
sys.stdin = open("baek1516.txt")

"""
백준 1005번과 동일한 문제! 
잘 이해하자

특정 건물을 지을때 선행 조건이 필요한 경우라면,
그 건물이 지어지는 '최소 시간' 은
각 선행 건물이 지어지는 최소시간의 합 + 해당 건물이 지어지는 건설 시간이 됨

따라서 새로운 선행 조건의 건물이 건설 될때마다 update 를 쳐주기 위해서
dp[next_node] = max(dp[next_node], dp[node]+next_cost) 를 진행하는것!
"""

N = int(input())
in_order = [0] * (N+1)

graph = [[] for _ in range(0, N+1)]
build_time = [0] * (N+1)

for i in range(0, N):
    tmp = list(map(int, input().split()))
    cost = tmp[0]
    pre_conditions = tmp[1:-1]
    build_time[i+1] = cost

    for pre_condition in pre_conditions:
        in_order[i+1] += 1
        graph[pre_condition].append(i+1)

INF = 987654321
dp = [INF] * (N+1)
for i in range(1, N+1):
    dp[i] = build_time[i]
que = deque()
for i in range(1, N+1):
    if in_order[i] == 0:
        que.append((i, cost))

while que:
    node, cost = que.popleft()

    for next_node in graph[node]:
        next_cost = build_time[next_node]
        # 이 부분이 핵심 '최소'시간이라고 무조건 min이 아니다!
        dp[next_node] = max(dp[next_node], dp[node]+next_cost)
        in_order[next_node] -= 1
        if in_order[next_node] == 0:
            que.append((next_node, dp[next_node]))

for i in range(1, N+1):
    print(dp[i])