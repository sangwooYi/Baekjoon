import sys
from collections import deque
sys.stdin = open("baek17220.txt")


N, M = map(int, input().split())
alph_to_idx = {}
for i in range(0, N):
    alph_to_idx[chr(i+65)] = i

graph = [[] for _ in range(0, N)]
in_order = [0] * N
for i in range(0, M):
    a, b = input().split()
    a_idx = alph_to_idx[a]
    b_idx = alph_to_idx[b]

    in_order[b_idx] += 1
    graph[a_idx].append(b_idx)

catch_list = input().split()
visited = [0] * N
for i in range(1, len(catch_list)):
    ban_idx = alph_to_idx[catch_list[i]]
    visited[ban_idx] = 1

answer = 0
que = deque()

for i in range(0, N):
    if in_order[i] == 0 and not visited[i]:
        que.append(i)
        visited[i] = 1

while que:
    node = que.popleft()

    for next_node in graph[node]:
        if visited[next_node]:
            continue
        answer += 1
        visited[next_node] = 1
        que.append(next_node)
print(answer)