import sys
sys.stdin = open("baek17270.txt")

"""
V 가 100이므로
플로이드 와샬 가능 ( 한번에 모든 노드간 최단거리를 알 수 있으나 O(N**3) 알고리즘..)

따라서 
플로이드 와샬 쓴 후, 모든 노드 체크

or 

다익스트라로 처음부터 모든 노드 체크해서 결과 체크

V가 100이라 둘다 될 듯

두 사람의 최단거리 합이 최소 이면서 지헌의 시간이 더 짧아야함 
=> 여러개라면 지헌이한테 가까운 쪽 => 여러개라면 가장 작은 노드
(이게 sort 순서)

여기서 함정! 
=> 조건을 따지는 순서가
1. 각자 출발점이 아니고, 2. 각자 최단거리의 합이 최소
이 두가지를 먼저 만족해야 한다
이 중에서 그다음 조건을 따지는것

즉 만약 전체 노드 중 최단거리합이 최소인 노드가 2 번인데
해당 경우에 지헌이가 더 늦게 도착한 경우 일 때.
=> 그냥 만나는게 불가능한것!
(그 다음 최소 노드를 찾을 수는 있으나, 전체 최소가 아니다! , 이부분이 함정..)
"""

V, M = map(int, input().split())
INF = 987654321

# 기껏해야 V가 100이므로 가능
graph = [[INF] * (V+1) for _ in range(0, V+1)]

for i in range(0, M):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    graph[b][a] = min(graph[b][a], c)

J, S = map(int, input().split())

for w in range(1, V+1):
    for s in range(1, V+1):
        for e in range(1, V+1):
            if s == e:
                graph[s][e] = 0
            graph[s][e] = min(graph[s][e], graph[s][w] + graph[w][e])


min_cost = INF
answer_candidates = []

for node in range(1, V+1):
    # 각자의 출발지는 제외
    if node == J or node == S:
        continue
    jihun_cost = graph[J][node]
    sungha_cost = graph[S][node]
    
    # 한명이라도 갈수 없으면 pass
    if jihun_cost == INF or sungha_cost == INF:
        continue
    
    cost_sum = jihun_cost + sungha_cost

    add_form = [jihun_cost, sungha_cost, node]
    if cost_sum < min_cost:
        min_cost = cost_sum
        answer_candidates = [add_form]
    elif cost_sum == min_cost:
        answer_candidates.append(add_form)
# 후보가 있을경우에만 체크
if len(answer_candidates) > 0:
    tmp_arr = []
    for i in range(0, len(answer_candidates)):
        jihun_cost, sungha_cost, node = answer_candidates[i]
        # 지헌이 더 오래걸리는 경우 제외
        if jihun_cost > sungha_cost:
            continue
        tmp_arr.append([jihun_cost, node])
    answer_candidates = tmp_arr

if len(answer_candidates) == 0:
    print(-1)
else:
    answer_candidates.sort(key=lambda x : (x[0], x[1]))
    print(answer_candidates[0][1])
