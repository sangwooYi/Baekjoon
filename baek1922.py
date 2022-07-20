import sys
sys.stdin = open("baek1922.txt")

"""
크루스칼로 MST 풀기

find - union

노드 정보 + cost 를 전부 저장,
cost 기준으로 오름차순 정렬
모든 코스트를 순차적으로 순회하며
아직 연결 안된 경우만 체크 find(a) != find(b)
연결 안되어있으면 union(a, b) 하고 cost 합산

Prim 이랑 비교!
프림은 모든 출발점에 대해서 체크해야하며
출발점이 정해지면, 해당 출발지에서 부터 우선순위 큐로 진행
현재 기준 가장 cost 낮은 애를 pop 한 후, DP[next] > DP[now] + cost 인 경우만 갱신
"""

def find(x):
    if x == parent[x]:
        return x
    px = find(parent[x])
    parent[x] = px
    return px

def union(x, y):
    px = find(x)
    py = find(y)
    # 작은 쪽에 병합
    if px > py:
        parent[px] = py
    else:
        parent[py] = px



N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
nodes = [0] * M
for i in range(0, M):
    s, e, c = map(int, sys.stdin.readline().split())
    nodes[i] = [s, e, c]
# cost 기준 오름차순
nodes.sort(key=lambda x : x[2])
parent = [i for i in range(0, N+1)]

answer = 0
for node in nodes:
    s, e, c = node
    if find(s) != find(e):
        union(s, e)
        answer += c
print(answer)