import sys
from collections import deque
sys.stdin = open("baek14615.txt")


def bfs1():
    visited1[1] = True
    
    que = deque()
    que.append(1)

    while que:
        node = que.popleft()
        for next_node in graph1[node]:
            if visited1[next_node]:
                continue
            visited1[next_node] = True
            que.append(next_node)

def bfs2():
    visited2[N] = True
    que = deque()
    que.append(N)

    while que:
        node = que.popleft()
        for next_node in graph2[node]:
            if visited2[next_node]:
                continue
            visited2[next_node] = True
            que.append(next_node)


N, M = map(int, sys.stdin.readline().split())
graph1 = [[] for _ in range(0, N+1)]
graph2 = [[] for _ in range(0, N+1)]
for i in range(0, M):
    # 방향성 그래프임!
    x, y = map(int, sys.stdin.readline().split())
    graph1[x].append(y)
    graph2[y].append(x)

T = int(sys.stdin.readline())

visited1 = [False] * (N+1)
visited2 = [False] * (N+1)

bfs1()
bfs2()

# 포인트는 TC 가 10만개라는 것이다.
# 따라서 TC 마다 bfs 돌리면 10만 * 10만이 되어버려 시간초과.. 한번에 구해야한다! 
# 따라서 역간선을 같이 체크해주는것!
# 문제 조건을 잘 보자!
for tc in range(0, T):
    C = int(sys.stdin.readline())

    if visited1[C] and visited2[C]:
        print("Defend the CTP")
    else:
        print("Destroyed the CTP")