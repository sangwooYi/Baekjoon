import sys
import heapq
sys.stdin = open("baek12441.txt")


def dijkstra(idx):

    dist = friend_path_each_node[idx]
    start_node = friend_start_point[idx]

    dist[start_node] = 0
    hq = []
    heapq.heappush(hq, (0, start_node))

    while hq:
        path, node = heapq.heappop(hq)

        for next_node, next_cost in graph[node]:
            if dist[next_node] <= path + next_cost:
                continue
            dist[next_node] = path+next_cost
            heapq.heappush(hq, (dist[next_node], next_node))

INF = 98765432198
T = int(input())
for tc in range(1, T+1):
    N, P, M = map(int, input().split())

    graph = [[] for _ in range(0, N+1)]
    req_time_per_path = [0] * P

    # i번 친구가 a 번 도시까지 가는데 걸리는 경로를 저장
    friend_path_each_node = [[INF] * (N+1) for _ in range(0, P)]
    friend_start_point = [0] * P

    for i in range(0, P):
        a, b = map(int, input().split())
        req_time_per_path[i] = b
        friend_start_point[i] = a

    for i in range(0, M):
        tmp = list(map(int, input().split()))
        D = tmp[0]
        L = tmp[1]
        nodes = tmp[2:]
        
        for j in range(0, L-1):
            s = nodes[j]
            e = nodes[j+1]
            graph[s].append((e, D))
            graph[e].append((s, D))
    
    for i in range(0, P):
        dijkstra(i)
    
    min_val = INF
    for i in range(1, N+1):
        req_time = 0
        for j in range(0, P):
            cur_path = friend_path_each_node[j][i]
            if cur_path == INF:
                req_time = INF
                break
            cur_req_time = cur_path*req_time_per_path[j]
            req_time = max(req_time, cur_req_time)
        min_val = min(min_val, req_time)
    if min_val == INF:
        min_val = -1
    print(f"Case #{tc}: {min_val}")