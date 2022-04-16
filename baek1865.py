import sys
sys.stdin = open("baek1865.txt")
"""
그냥 BFS???
 
아이디어1.
그냥 start 1 -> N번노드까찌 순회하면서
이 중, DP[start] < 0 이 나오는게 있는지 체크
(노드 500개, 최대 간선수 2500개라서 가능할지도/..???)

다익스트라는 음수값 처리 안된다!
이땐 벨만-포드 알고리즘 => 아예 다익스트라랑 구현방식이 다르다!!

문제 잘 읽자.. 
도로는 방향이 있고, 웜홀은 방향이 없다
"""

def worm_hole(graph, n, start):
    INF = 9876543
    dis = [INF] * (n+1)
    dis[start] = 0

    for i in range(0, n):
        for s in range(1, n+1):
            for next_node, next_cost in graph[s]:
                if dis[next_node] > dis[s] + next_cost:
                    dis[next_node] = dis[s] + next_cost
                    if i == n-1:
                        return True
    return False

T = int(input())
for tc in range(1, T+1):
    N, M, W = map(int, sys.stdin.readline().split())
    G = [[] for _ in range(0, N+1)]

    for i in range(0, M):
        a, b, c = map(int, input().split())
        G[a].append((b, c))
        G[b].append((a, c))
    for i in range(0, W):
        a, b, c = map(int, input().split())
        G[a].append((b, -c))

    is_pos = worm_hole(G, N, 1)
    if is_pos:
        print("YES")
    else:
        print("NO")