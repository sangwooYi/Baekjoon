import sys
import heapq
sys.stdin = open("baek1466.txt")


"""
그냥 DP 문제다..
DP 문제도 다시 풀어보자

DP 풀이
short_cuts = [0] * N

for i in range(0, N):
    s, e, cost = map(int, input().split())
    
    short_cuts[i] = (s, e, cost)

# 0부터 D까지 쭉 순회
for i in range(0, D+1):
    # DP[i-1] 에서 그냥 왔을떄와 DP[i] 까지 현재 저장값중 최솟값을
    # 매번 갱신
    if i > 0:
        DP[i] = min(DP[i], DP[i-1]+1)

    for s, e, cost in short_cuts:
        if e > D:
            continue
        if s == i:
            DP[e] = min(DP[e], DP[i]+cost)
print(DP[D])

"""

"""
아래는 heapq로 풀이

그냥 쫄지말고 풀자...
"""
N, D = map(int, input().split())
DP = [i for i in range(0, D+1)]

graph = [[] for _ in range(0, D+1)]
for i in range(0, D):
    graph[i].append((i+1, 1))

for i in range(0, N):
    s, e, cost = map(int, input().split())
    if e > D:
        continue
    graph[s].append((e, cost))
INF = 987654321
dist = [INF] * (D+1)

hq = []
dist[0] = 0
# 현재까지 cost를 기준으로  heapq
heapq.heappush(hq, (0, 0))

while hq:
    cost, node = heapq.heappop(hq)

    # 현재 저장된 dist보다 큰값이면 pass
    if cost > dist[node]:
        continue

    for next_node, next_cost in graph[node]:
        
        if dist[next_node] <= cost+next_cost:
            continue
        dist[next_node] = cost + next_cost
        heapq.heappush(hq, (dist[next_node], next_node))
print(dist[D])