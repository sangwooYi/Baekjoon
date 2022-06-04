import sys
import heapq
sys.stdin = open("baek1647.txt")


"""
MST 중 크루스칼 알고리즘 문제!

크루스칼은 find / union 이용
1. 가중치 순으로 오름차순 정렬
2. 해당 edge들을 순회하면서, 부모 노드가 다를경우만 간선에 추가!
    ( px != py 일때만)
이게 전부이다! (이름만 어렵지 알고리즘 자체는 쉽다 꼭 기억해 둘 것!)

프림 알고리즘의 경우는 시작 노드에 따라 결과가 다르다!
따라서, 프림알고리즘 정석은
시작노드를 존재하는 모든 노드에 대해 체크하고,
그 중 최솟값을 찾아야 진짜 MST가 찾아지는것!
물론. 시작 노드가 정해진 문제라면 예외

크루스칼은 그에 비해, 한번에 MST 를 찾아준다

따라서, 시작 노드가 정해져 있다면 
=> 프림 알고리즘이 더 효율적 
(우선순위 큐를 써서, 정렬할 필요가 없으므로)
아니라면, 크루스칼이 훨씬 효율적! 

둘다 쓸줄 알아야 한다!

프림은 heapq 이용한 그리디!
크루스칼은 find - union 이용!
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
sum = 0
max_cost = 0
for i in range(0, len(result)):
    if max_cost < result[i]:
        max_cost = result[i]
    sum += result[i]
answer = sum-max_cost
print(answer)



