import sys
import heapq
sys.stdin = open("baek1504.txt")
"""
1 => N번 정점으로 가는데,
그 중에 반드시 거쳐야 하는 노드가 존재.

아이디어1.
    1-> u -> v -> N  // 1 -> v -> u -> N 
    가능한것 중 최솟값
    얘네도 안되면 그냥 안되는거 -1반환 
    노드가 800개라 충분히 가능
다익스트라 사용할때, 도착했다고 바로 그 값을 return하지는 말자!
그냥 다 돌린다음에 DP[노드] 값을 반환하는게 안전!
"""


def find_path(graph, n, start, goal):
    # 그냥 이동
    hq = []
    INF = 987654321
    DP = [INF] * (n+1)
    DP[start] = 0
    heapq.heappush(hq, (0, start))
    while hq:
        cost, node = heapq.heappop(hq)
        if cost > DP[node]:
            continue
        for next_node, next_cost in graph[node]:
            if DP[next_node] < DP[node] + next_cost:
                continue
            DP[next_node] = DP[node] + next_cost
            heapq.heappush(hq, (DP[next_node], next_node))
    # 다익스트라 쓸때, 왠만하면 그냥 다 돌리고 이렇게 return 하자
    # 중간에 노드 도착했다고 바로 return해버리면 다른 최소경로가 나타날수있다!
    # ex) 바로 도착한 cost가 100 인데, 다른 노드 거쳐서 간 cost가 20일수도!
    return DP[goal]



N, E = map(int, sys.stdin.readline().split())
G = [[] for _ in range(0, N+1)]
for i in range(0, E):
    a, b, c = map(int, sys.stdin.readline().split())
    G[a].append((b, c))
    G[b].append((a, c))
U, V = map(int, sys.stdin.readline().split())

# 1 -> u -> v -> N
a = find_path(G, N, 1, U) 
b = find_path(G, N, U, V) 
c = find_path(G, N, V, N)
d = find_path(G, N, 1, V) 
e = find_path(G, N, V, U) 
f = find_path(G, N, U, N)

path1 = a + b + c
path2 = d + e + f
# 이부분이 아이디어이다! 어차피 못들른곳이 있었다면 INF값보다는 합이 커졌을것
if path1 >= 987654321 and path2 >= 987654321:
    print(-1)
# 둘중에 하나만이라도 아니면, 그냥 min값 뽑아내면 된다.
else:
    print(min(path1, path2))

