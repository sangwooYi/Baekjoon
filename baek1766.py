import sys
import heapq
sys.stdin = open("baek1766.txt")

"""
먼저 풀어야하는 문제가 있으면 먼저 풀어야 한다.
가능하면 쉬운문제부터

아이디어1.
먼저 풀어야하는 애들을 heapq에 저장
+ in_degree 추가

위상 정렬을 그냥 우선순위 큐로 푸는 문제였다!

위상정렬 방법
1. 진입 차수 체크
2. 진입차수 = 0인 애를 큐에 저장
3. pop 해서 나온 현재노드에서 갈 수 있는  next 노드들 체크하여 next 노드의 진입 차수 -= 1
4. next 노드의 진입차수가 0이 된다면 그 노드는 큐에 저장

여기서 큐를 우선순위큐로 쓰면 되는 문제였다 (가능한 쉬운 문제부터 풀어야 하므로)
"""

N, M = map(int, input().split())
in_degree = [0] * (N+1)
graph = [[] for _ in range(0, N+1)]
hq = []


visited = [False] * (N+1)
for i in range(0, M):
    a, b = map(int, input().split())
    graph[a].append(b)
    # 진입차수 증가
    in_degree[b] += 1

answer = []

for i in range(1, N+1):
    # 진입차수 0인애들을 저장 (시작점)
    if in_degree[i] == 0:
        heapq.heappush(hq, i)
    
while hq:
    # 우선 순위 큐를 썼기 때문에, 무조건 현재 기준 최소 node부터 나온다.
    node = heapq.heappop(hq)
    answer.append(node)
    # 현재 노드에서 갈 수 있는 next 노드들 체크
    for next_node in graph[node]:
        # 진입차수 -1 
        in_degree[next_node] -= 1
        # 만약 진입차수 0이 된 노드가 있으면 우선순위 큐에 저장
        if in_degree[next_node] == 0:
            heapq.heappush(hq, next_node)

print(" ".join(map(str, answer)))