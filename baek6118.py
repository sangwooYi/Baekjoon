import sys
sys.stdin = open("baek6118.txt")
from collections import deque

"""
오히려 가장 먼 거리를 찾아야 함
"""

def check_route():
    
    visited[1] = 0
    que = deque()
    que.append((1, 0))

    while que:
        node, path = que.popleft()

        for next_node in graph[node]:
            if visited[next_node] == -1:
                visited[next_node] = path+1
                que.append((next_node, path+1))


N, M = map(int, input().split())
graph = [[] for _ in range(0, N+1)]


visited = [-1] * (N+1)
for i in range(0, M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
check_route()

max_len = 0
cnt = 0
min_node = 0

for i in range(2, N+1):
    cur_len = visited[i]

    if cur_len > max_len:
        max_len = cur_len
        cnt = 1
        min_node = i
    elif cur_len == max_len:
        cnt += 1
print(min_node, max_len, cnt)