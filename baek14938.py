import sys
import heapq
sys.stdin = open("baek14938.txt")
"""
다익스트라 or 플로이드 와샬로 푸는 문제라고 합니다.
다익스트라 로직에서 도착 노드에 따른 종료조건이 없으면
시작 노드부터 -> 특정 노드까지 최단 경로값이 전부 구해진다!!!!
다익스트라의 개념을 잘 이해할것!!

특정 노드간의 최단 경로를 찾아야 하는경우는 다익스트라 꼭 사용해야함!
안그러면 최단 가중값 탐색이 제대로 안이루어짐!

잘 정리해 둡시다! 문제 잘 읽고 필요한 개념을 잘 꺼내 쓸 수 있어야함
최소신장트리 => MST
노드 간 가중치가 존재할때 최단 가중값 => 다익스트라
가중치 없을 때, 그냥 최단 경로를 구할 때 => BFS
"""

def dijkstra(s, n, graph):
    hq = []
    dist = [INF] * (n+1)
    heapq.heappush(hq, (0, s))
    dist[s] = 0
    while hq:
        now_cost, now_node = heapq.heappop(hq)
        for cost, next_node in graph[now_node]:
            # dp 개념
            if dist[now_node] + cost > dist[next_node]:
                continue
            dist[next_node] = dist[now_node] + cost
            heapq.heappush(hq, (dist[next_node], next_node))
    return dist

N, M, R = map(int, input().split())
I = list(map(int, input().split()))
INF = 987654321
# 그래프 만들때 아래와같이 만들것 (노드 시작을 0번노드부터 시작하던, 1번 노드부터 시작하던)
G = [[] for _ in range(0, N+1)]

# 양방향 그래프 (이건 문제 반드시 잘 읽기)
for i in range(0, R):
    a, b, c = map(int, input().split())
    G[a].append((c, b))
    G[b].append((c, a))
max_count = 0

for i in range(1, N+1):
    res = dijkstra(i, N, G)
    temp = 0
    for j in range(1, N+1):
        if res[j] <= M:
            temp += I[j-1]
    if max_count <= temp:
        max_count = temp
print(max_count)
