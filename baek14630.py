import sys
import heapq
sys.stdin = open("baek14630.txt")


def calc_term(a_str, b_str, size):
    res = 0
    
    for i in range(0, size):
        now = (int(a_str[i]) - int(b_str[i]))**2
        res += now
    return res

def dijkstra(start, end, graph):
    size = len(graph)
    INF = 987654321
    dist = [INF] * size
    dist[start] = 0

    hq = []
    heapq.heappush(hq, (0, start))

    while hq:
        cost, node = heapq.heappop(hq)
        if dist[node] < cost:
            continue
        for next_node, next_cost in graph[node]:
            if dist[next_node] <= dist[node] + next_cost:
                continue
            dist[next_node] = dist[node]+next_cost
            heapq.heappush(hq, (dist[next_node], next_node))
    return dist[end]



N = int(input())
nodes = [0] * N
for i in range(0, N):
    nodes[i] = input()
part_len = len(nodes[0])

A, B = map(int, input().split())
A -= 1
B -= 1
tmp_dict = {}
graph = [[] for _ in range(0, N)]

for i in range(0, N):
    for j in range(i+1, N):
        term = calc_term(nodes[i], nodes[j], part_len)
        graph[i].append((j, term))
        graph[j].append((i, term))

answer = dijkstra(A, B, graph)
print(answer)