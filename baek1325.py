import sys
from collections import deque
sys.stdin = open("baek1325.txt")


def bfs(start_node):
    que = deque()
    visited = [False] * (N+1)
    visited[start_node] = True
    que.append(start_node)
    cnt = 0

    while que:
        node = que.popleft()

        for next_node in graph[node]:
            if visited[next_node]:
                continue
            visited[next_node] = True
            cnt += 1
            que.append(next_node)
    return cnt



N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(0, N+1)]

for _ in range(0, M):
    #  b -> a 로 해킹 가능
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)

check_arr = [0] * (N+1)
check_arr[0] = [0, 0]

for i in range(1, N+1):
    cur_cnt = bfs(i)
    check_arr[i] = [i, cur_cnt]

check_arr.sort(key=lambda x : (-x[1], x[0]))

max_cnt = check_arr[0][1]

for i in range(0, N+1):
    if check_arr[i][1] != max_cnt:
        break
    print(check_arr[i][0], end=" ")