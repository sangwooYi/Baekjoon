import sys
from collections import deque
sys.stdin = open("baek13463.txt")



# C 총 마을 수, P 주어지는 간선 수, X 내 마을, L 탈출 시작한 마을
C, P, X, L = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(0, C+1)]
limit_arr = [0] * (C+1)
# 내 주변에 탈출한 마을수를 체크
neig_leave_cnt = [0] * (C+1)
visited = [False] * (C+1)
for i in range(0, P):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, C+1):
    neighbor_cnt = len(graph[i])

    cur_limit = neighbor_cnt//2
    if neighbor_cnt%2:
        cur_limit += 1
    limit_arr[i] = cur_limit

visited[L] = True
for node in graph[L]:
    neig_leave_cnt[node] += 1
que = deque()
que.append(L)

while que:
    node = que.popleft()

    for next_node in graph[node]:
        if visited[next_node]:
            continue
        limit_cnt = limit_arr[next_node]

        cnt = neig_leave_cnt[next_node]
        if cnt >= limit_cnt:
            visited[next_node] = True

            for chk_node in graph[next_node]:
                neig_leave_cnt[chk_node] += 1
            que.append(next_node)
if visited[X]:
    print("leave")
else:
    print("stay")