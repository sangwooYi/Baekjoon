import sys
from collections import deque
sys.stdin = open("baek14248.txt")


N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
S = int(sys.stdin.readline().rstrip())

visited = [False] * N
que = deque()
visited[S-1] = True
que.append(S-1)
cnt = 1

d = [-1, 1]

while que:
    node = que.popleft()

    term = arr[node]

    for i in range(0, 2):

        next_node = node + d[i]*term

        if next_node < 0 or next_node >= N:
            continue
        if visited[next_node]:
            continue
        visited[next_node] = True
        cnt += 1
        que.append(next_node)
print(cnt)