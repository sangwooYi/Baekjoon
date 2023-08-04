import sys
from collections import deque
sys.stdin = open("baek19538.txt")


"""
주변인 절반이 루머를 믿고있을때 믿게된다.
"""

def bfs():

    que = deque()
    for start_node in start_nodes:
        visited[start_node] = 0
        que.append(start_node)
    
    path = 0
    while True:
        path += 1
        tmp_que = deque()
        while que:

            node = que.popleft()

            for next_node in graph[node]:
                
                if visited[next_node] != -1:
                    continue

                limit = chk_arr[next_node]
                cnt = 0
                
                for around in graph[next_node]:
                    if visited[around] != -1:
                        cnt += 1
                if cnt >= limit:
                    tmp_que.append(next_node)
        # 종료 시점
        if len(tmp_que) == 0:
            return
        while tmp_que:
            node = tmp_que.popleft()
            visited[node] = path
            que.append(node)

                

N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(0, N+1)]
visited = [-1] * (N+1)
# 믿는 경계선 저장
chk_arr = [0] * (N+1)

for i in range(1, N+1):
    tmp = list(map(int, sys.stdin.readline().split()))
    # 길이가 1이면 아무 경로도 없는것
    if len(tmp) > 1:
        nodes = tmp[:-1]
        
        for node in nodes:
            # 반대편 경로도 다음에 또 주어지므로 단방향으로만 저장
            graph[i].append(node)

for i in range(1, N+1):
    around_cnt = len(graph[i])

    bound_limit = around_cnt//2
    if around_cnt%2:
        bound_limit += 1
    chk_arr[i] = bound_limit

M = int(sys.stdin.readline().rstrip())
start_nodes = list(map(int, sys.stdin.readline().split()))

bfs()
print(" ".join(map(str, visited[1:])))