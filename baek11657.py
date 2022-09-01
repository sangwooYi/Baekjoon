import sys
sys.stdin = open("baek11657.txt")


"""
벨만포드 알고리즘 연습!

1부터 N까지 모든 노드에 대해,
현재 노드에 갈 수 있는 모든 간선들을 체크
D[next_node] > D[현재노드] + cost 일때마다 갱신
이걸 N번 반복함!

다익스트라가 음수  cost가 나오면 풀수 없기때문에
그 대안으로 나오는 알고리즘! (단 O(N**2)임)
"""


def bellman_ford(graph, n):
    
    dis[1] = 0

    for i in range(0, n):
        for s in range(1, n+1):
            for next_node, cost in graph[s]:
                # dis[s] != INF 체크 조건 들어가야함! (어차피 현재 노드까지가 INF면 못가니까!)
                if dis[s] != INF and dis[next_node] > dis[s] + cost:
                    dis[next_node] = dis[s] + cost
                    # N번만큼 반복했는데도 갱신되었다면 음수사이클이 발생한것! (벨만포드의 핵심)
                    if i == n-1:
                        return True
    return False
 

N, M = map(int, input().split())
graph = [[] for _ in range(0, N+1)]
for i in range(0, M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
INF = 987654321
dis = [INF] * (N+1)


is_negative = bellman_ford(graph, N)

if is_negative:
    print(-1)
else:
    for i in range(2, N+1):
        if dis[i] == INF:
            print(-1)
        else:
            print(dis[i])
