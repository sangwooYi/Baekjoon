import sys
from collections import deque
sys.stdin = open("baek11060.txt")


def bfs():
    INF = 987654321
    visited = [INF] * N
    visited[0] = 0
    que = deque()
    que.append(0)

    while que:
        node = que.popleft()

        jump = jump_map[node]

        for i in range(1, jump+1):
            next_node = node + i
            if next_node >= N:
                continue
            if visited[next_node] <= visited[node]+1:
                continue
            visited[next_node] = visited[node]+1
            que.append(next_node)
    if visited[N-1] == INF:
        return -1
    return visited[N-1]


N = int(input())
jump_map = list(map(int, input().split()))

answer = bfs()

print(answer)
