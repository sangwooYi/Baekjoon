import sys
import heapq


"""
크루스칼 알고리즘
1. 간선 가중치에 따른 오름차순 정렬
2. 정렬한 edge를 전부 순회
3. if (find[x] != find[y]) 일 경우에만 (부모노드가 서로 다른경우에만)
   간선에 추가. (union 처리 + cost 추가)


프림 알고리즘
1. 존재하는 노드를 차례대로 순회, 현재 차례의 노드가 시작노드가 됨
2. 시작노드 방문처리
3. 해당 노드에서 갈 수 있는 모든 간선 heapq 에 push
4. pop 된 애들은 cost 추가 해주고, 해당 노드에서 갈 수 있는 모든 방향 체크
   => 방문처리, heapq에 push
5. heapq 순회 끝난 이후에 cost 합산값과, 현재까지의 min_path 중 작은값으로 min_path 갱신
   (min_path = min(min_path, now_path))

기본적으로 시작노드가 정해지지 않은 경우에는
크루스칼 알고리즘이 훨씬 효율적이다!
하지만 시작노드가 정해진 문제라면,
프림알고리즘이 정렬할 필요가 없어서 오히려 더 효율적!


따라서 시작노드가 정해진 문제라면 => 프림
       아니면 => 크루스칼

주의 할 것이 시작노드가 정해진 문제에서의 프림알고리즘 값이
=> 해당 그래프에서 최선의 MST는 아니다! 이부분 주의!

"""



# 크루스칼 알고리즘 
def find(x):
    if x == parent[x]:
        return x
    px = find(parent[x])
    parent[x] = px

    return px


def union(x, y):
    px = find(x)
    py = find(y)
    if px > py:
        parent[px] = py
    else:
        parent[py] = px

N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(0, N+1)]
# 크루스칼 알고리즘!
edges = [0] * M
result = []
for i in range(0, M):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[i] = (c, a, b)
# 가중치 순으로 정렬
edges.sort()
for i in range(0, len(edges)):
    cost, f, t = edges[i]
    # 서로 부모노드가 다를 경우만 간선 추가 (부모노드가 같다면 이미 이어져 있는 상태라는 것)
    if find(f) != find(t):
        union(f, t)
        result.append(cost)




# MST 알고리즘 중 Prim 알고리즘! 
graph = [[] for _ in range(0, N+1)]
min_path = 987654321
# 시작노드를 전부 다르게 해야 한다. 
for i in range(1, N+1):
    visited = [False] * (N+1)
    visited[i] = True
    hq = []
    path = 0
    for c, n in graph[i]:
        heapq.heappush(hq, (c, n))
    
    while hq:
        cost, node = heapq.heappop(hq)
        if visited[node]:
            continue
        visited[node] = True
        path += cost
        for next_cost, next_node in graph[node]:
            if visited[next_node]:
                continue
            heapq.heappush(hq, (next_cost, next_node))
    # 기존 min_path 값보다 작은 값이 나왔다면 갱신
    if path < min_path:
        min_path = path
