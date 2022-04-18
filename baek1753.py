import sys
import heapq
sys.setrecursionlimit(20000)
sys.stdin = open("baek1753.txt")
"""
방향 그래프!!

노드가 많은 경우에는 기존 방법으로는 메모리 초과 발생 가능.
따라서
다익스트라 작성할떄 for문 돌리기 전,
if DP[node] < cost:
    continue
이부분도 꼭 붙여줄것!
효율화 차이가 좀 발생한다! 습관들이자!
"""
def dijkstra(graph, v, start):
    hq = []
    INF = 987654
    DP = [INF] * (v+1)
    DP[start] = 0
    heapq.heappush(hq, (0, start)) 
    while hq:
        now = heapq.heappop(hq)
        cost = now[0]
        node = now[1]
        # 다익스트라 좀더 효율화 현재 DP 값보다 cost가 더 크면 아예 밑의 for문 돌릴 이유도 X 
        if DP[node] < cost:
            continue
        for next_node, next_cost in graph[node]:
            if DP[next_node] < DP[node] + next_cost:
                continue
            DP[next_node] = DP[node] + next_cost
            heapq.heappush(hq, (DP[next_node], next_node))
    result = [0] * v
    for i in range(0, v):
        if i == start-1:
            result[i] = 0
        else:
            if DP[i+1] == INF:
                result[i] = "INF"
            else:
                result[i] = DP[i+1]
    return result


V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
G = [[] for _ in range(0, V+1)]
for i in range(0, E):
    a, b, c = map(int, sys.stdin.readline().split())
    G[a].append((b, c))
ans = dijkstra(G, V, K)
for i in range(0, len(ans)):
    print(ans[i])