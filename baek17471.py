import sys
from collections import deque
sys.stdin = open("baek17471.txt")


def is_linked(arr):

    que = deque()
    visited = [False] * len(arr)
    start = arr[0]
    que.append(start)
    visited[0] = True
    
    node_cnt = len(arr)

    idx_dict = {}
    for i in range(0, node_cnt):
        idx_dict[arr[i]] = i
    cnt = 0
    while que:
        node = que.popleft()
        for next_node in graph[node]:
            if next_node not in idx_dict.keys():
                continue
            idx_conv = idx_dict[next_node]
            if visited[idx_conv]:
                continue
            visited[idx_conv] = True
            que.append(next_node)
            cnt += 1
    if cnt < node_cnt-1:
        return False
    return True

def comb(arr, visited, start, n, r, k):
    global answer

    if r == 0:
        area1 = [0] * k
        area2 = [0] * (n-k)
        idx1 = 0
        idx2 = 0
        for i in range(0, n):
            if visited[i]:
                area1[idx1] = arr[i]
                idx1 += 1
            else:
                area2[idx2] = arr[i]
                idx2 += 1
        if is_linked(area1) and is_linked(area2):
            area1_sum = 0
            area2_sum = 0
            for i in range(0, k):
                area1_sum += populations[area1[i]]
            for i in range(0, (n-k)):
                area2_sum += populations[area2[i]]
            tmp_sub = abs(area1_sum-area2_sum)
            answer = min(answer, tmp_sub)
        return
    for i in range(start, n):
        if visited[i]:
            continue
        visited[i] = True
        comb(arr, visited, i+1, n, r-1, k)
        visited[i] = False


N = int(input())
populations = [0] + list(map(int, input().split()))
graph = [[] for _ in range(0, N+1)]
for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    if tmp[0] > 0:
        nodes = tmp[1:]
        for node in nodes:
            graph[i].append(node)

mid = N//2

INF = 987654321
answer = INF
tmp_arr = [i for i in range(1, N+1)]
for i in range(1, mid+1):
    visited = [False] * N
    comb(tmp_arr, visited, 0, N, i, i)
if answer == INF:
    answer = -1
print(answer)