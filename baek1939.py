import sys
from collections import deque
sys.stdin = open("baek1939.txt")


"""
가능한 최대치를 구하는 문제이므로,
조건을 만족해도 값을 키운다. (upper bound)
"""


def is_possible(weight):

    visited = [False] * (N+1)
    visited[S] = True
    que = deque()
    que.append(S)

    while que:
        node = que.popleft()
        if node == E:
            return True
        for next_node, weight_limit in graph[node]:

            if weight_limit < weight:
                continue
            if visited[next_node]:
                continue
            visited[next_node] = True
            que.append(next_node)
    return False

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(0, N+1)]

# 같은 노드 사이의 여러 경로가있다면, 최댓값을 저장하자
temp_dict = {}
for i in range(0, M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


S, E = map(int, sys.stdin.readline().split())

# upper bound, lower bound 할때 최대치 +1로 시작해야한다! (이부분 주의)
left = 1
right = 1000000001
while left < right:
    mid = (left+right)//2

    if is_possible(mid):
        left = mid+1
    else:
        right = mid

print(left-1)

