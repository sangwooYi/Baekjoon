import sys
import heapq
sys.stdin = open("baek10282.txt")

INF = 987654321
T = int(input())
for tc in range(0, T):
    N, D, C = map(int, input().split())
    graph = [[] for _ in range(0, N+1)]
    for i in range(0, D):
        # b => a방향으로 이어지는것 . 같은 a, b 순서는 한번만 나옴
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    
    DP = [INF] * (N+1)
    DP[C] = 0
    hq = []
    heapq.heappush(hq, (0, C))

    while hq:
        cost, node = heapq.heappop(hq)

        for next_node, next_cost in graph[node]:
            if DP[next_node] <= next_cost + DP[node]:
                continue
            DP[next_node] = DP[node] + next_cost
            heapq.heappush(hq, (DP[next_node], next_node))
    
    cnt = 0
    max_time = 0
    for i in range(1, N+1):
        if DP[i] != INF:
            cnt += 1
            max_time = max(max_time, DP[i])
    print(f"{cnt} {max_time}")