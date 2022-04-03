import sys
sys.stdin = open("baek1005.txt")
"""
아이디어1. (노드가 1000개라서 가능할지 사실 의문이긴 함. 최악의경우 깊이 1000까지 가야하므로 ㄷㄷ.) 
목표지점이 출발점이된다.
=> 이동 가능한 노드를 전부저장
=> 없으면 그냥 바로 본인 cost가 정답
=> 이동 가능한노드 존재시, 전부 탐색
=> 갈곳이 없을떄까지 탐색해야함
=> DFS를 통해 깊이탐색이 더 효율적일듯? 
=> 이미 방문한 지점이라면, 저장된값보다 클때만 업데이트 (문제 특성상 더 오래걸리는쪽이 그 노드까지 도달시간이 된다!)
=> 방문 가능한 최종노드들에 저장된 시간중에서 최솟값을 출력

시간초과네 ..
"""


def acm_craft(graph, costs, visited, now, cost):
    flag = True
    for next_node in graph[now]:
        if visited[next_node]:
            continue
        visited[next_node] = True
        # 오히려 더 짧은시간이면 굳이 갈 필요가없음 
        if DP[now] + costs[next_node-1] < DP[next_node]:
            continue
        DP[next_node] = DP[now] + costs[next_node-1]
        next_cost = cost + costs[next_node-1]
        acm_craft(graph, costs, visited, next_node, next_cost)
        visited[next_node] = False
    # 더이상 갈곳이 없는것
    if flag:
        # 아직 아무도 안들른것
        if DP[now] == 0:
            DP[now] = cost
        else:
            if DP[now] < cost:
                DP[now] = cost
        return

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 코스트는 인덱스로 탐색 따라서 1차이남 조심!
    C = list(map(int, input().split()))
    DP = [0] * (N+1)
    check = [False] * (N+1)
    G = [[] for _ in range(0, N+1)]
    for i in range(0, K):
        # 건설 순서이므로, 단방향 그래프인것
        # 근데 나는 거꾸로 역방향 탐색하기로 했으므로 아래와같이 저장
        a, b = map(int, sys.stdin.readline().split())
        G[b].append(a)
    W = int(input())
    DP[W] = C[W-1]
    # 모두가 연결되어있다면 위와같은 풀이가 안먹힘
    acm_craft(G, C, check, W, C[W-1])
    answer = 0
    for i in range(1, len(DP)):
        if DP[i] == 0:
            continue
        if answer <= DP[i]:
            answer = DP[i]
    print(answer)