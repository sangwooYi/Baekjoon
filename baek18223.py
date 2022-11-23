import sys
import heapq
sys.stdin = open("baek18223.txt")

"""
1 => V 까지 최단 거리
1 => P 최단거리  + P => V 최단 거리의 합이
같은 경우만 구할 수 있음!

양방향, 같은 노드 쌍을 갖는 간선이 중복해서 주어지지 않음
"""

def dijkstra(start, end):

    dist = [INF] * (V+1)
    dist[start] = 0

    hq = []
    heapq.heappush(hq, (0, start))
    while hq:
        cost, node = heapq.heappop(hq)

        if cost > dist[node]:
            continue

        for next_node, next_cost in graph[node]:
            if dist[next_node] <= cost+next_cost:
                continue
            dist[next_node] = cost+next_cost
            heapq.heappush(hq, (dist[next_node], next_node))
    return dist[end]
 

V, E, P = map(int, input().split())
graph = [[] for _ in range(0, V+1)]
for i in range(0, E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

INF = 987654321
min_path = dijkstra(1, V)
part1 = dijkstra(1, P)
part2 =  dijkstra(P, V)

if part1 + part2 <= min_path:
    answer = "SAVE HIM"
else:
    answer = "GOOD BYE"
print(answer)