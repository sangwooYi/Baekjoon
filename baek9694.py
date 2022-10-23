import sys
import heapq
sys.stdin = open("baek9694.txt")

"""
다익스트라는 
가중치가 주어지는 간선에서의 최소 cost 를 구하는 문제!
따라서 heapq를 사용한다!
=> 매번 저장된 값중에 가장 적은 cost를 (heapq는 최소힙) 뽑아서
그 다음 경로를 체크 + 현재까지 cost+다음경로까지cost < 다음 노드에 저장된 cost 일때만 진행
=> 이게 다익스트라!!

(만약 가중치가 같다면 큐를 써도 무관)
단, 음수 가중치가 주어진다면 다익스트라를 쓸 수없다.
음수 가중치는 벨만포드 알고리즘!

경로 추적하는 방법 잘 기억해두자! (리스트처럼 서로의 경로를 저장해두는 형식)

다익스트라, 벨만포드, 워셜 다시 공부하자 ㅠㅠ
"""

def find_min(graph, m):
    DP = [INF] * m
    hq = []
    DP[0] = 0
    heapq.heappush(hq, (0, 0))

    while hq:
        cost, node = heapq.heappop(hq)
        if cost > DP[node]:
            continue
        for next_node, next_cost in graph[node]:
            if DP[next_node] <= cost+next_cost:
                continue
            DP[next_node] = cost+next_cost
            # 경로 저장!! 이부분 기억하자
            path[next_node] = node
            heapq.heappush(hq, (DP[next_node], next_node))

    return DP[M-1]

T = int(input())
for tc in range(1, T+1):
    # N이 관계의수, M이 정치인수 0이 나, M-1이 최고위원
    N, M = map(int, input().split())
    INF = 987654321
    graph = [[] for _ in range(0, M)]
    path = [-1] * M
    for i in range(0, N):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    result = find_min(graph, M)
    if result == INF:
        answer = -1
    else:
        pt = M-1
        tmp = [M-1]
        while pt > 0:
            node = path[pt]
            tmp.append(node)
            pt = node
        answer = " ".join(map(str, tmp[::-1]))
    print(f"Case #{tc}: {answer}")