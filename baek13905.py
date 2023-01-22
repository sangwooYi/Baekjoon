import sys
from collections import deque
sys.stdin = open("baek13905.txt")


# 크루스칼/MST로도 풀 수있다고 한다..

# 풀이방법 1 이분탐색
def is_possible(weight):

    visited = [False] * (N+1)
    que = deque()

    visited[S] = True
    que.append(S)

    while que:
        node = que.popleft()

        if node == E:
            return True

        for next_node, next_limit in graph[node]:

            if weight > next_limit:
                continue
            if visited[next_node]:
                continue
            visited[next_node] = True
            que.append(next_node)
    return False


N, M = map(int, sys.stdin.readline().split())
S, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(0, N+1)]

for i in range(0, M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

left = 1
right = 1000001

while left < right:
    mid = (left+right)//2

    if is_possible(mid):
        left = mid+1
    else:
        right = mid
print(left-1)


