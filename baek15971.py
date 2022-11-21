import sys
from collections import deque
sys.stdin = open("baek15971.txt")

"""
'임의의 두 방 사이를 이동할 때 같은 통로를 두 번 이상 지나지 않는 경로는 유일한 것'
=> 사이클이 없다는 의미인듯?
아이디어1.
우선 로봇 위치가 같게 주어진 경우는 그냥 
예외처리 (무조건 0)
=> 그다음 경우부터 진행 (따라서 이경우 최소 노드 2개)
로봇 하나 먼저 BFS 진행
=> 각 노드마다 이동 경로 저장

그 다음 로봇이 BFS 진행
매 다음 이동 가능한 다음 노드마다
1번로봇의 다음 노드까지 이동 거리 + 현재까지 2번로봇 이동거리 체크

매번 최솟값 갱신 (최솟값이 어떤 포인트에서 발생하는지를 묻지는 않고 있음)

10만 + 10만 이므로 O(N) 알고리즘. 충분히 가능?
"""


def find_min_path(graph, r1, r2):

    n = len(graph)-1
    que = deque()

    result = 9987654321
    robot1_dist = [-1] * (n+1)
    robot2_dist = [-1] * (n+1)
    robot1_dist[r1] = 0
    robot2_dist[r2] = 0

    que.append(r1)

    # 우선 1번로봇 진행
    while que:
        node = que.popleft()

        for next_node, next_cost in graph[node]:
            # 방문하지 않은 경우만 체크
            if robot1_dist[next_node] == -1:
                robot1_dist[next_node] = robot1_dist[node] + next_cost
                que.append(next_node)

    # 2번 로봇 진행
    que.append(r2)
    while que:
        node = que.popleft()

        for next_node, next_cost in graph[node]:
            # 이동 가능한 다음 노드에 대해서 1번 로봇과 이동경로 합 체크
            # 2번로봇의 현재 노드까지의 이동거리 + 2번로봇이 이동가능한 다음 노드까지 1번로봇의 이동거리
            if robot2_dist[next_node] == -1:
                tmp_sum = robot2_dist[node] + robot1_dist[next_node]
                result = min(result, tmp_sum)
                robot2_dist[next_node] = robot2_dist[node] + next_cost
                que.append(next_node)
    return result

N, robot1, robot2 = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(0, N+1)]
for i in range(0, N-1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
if robot1 == robot2:
    answer = 0
else:
    answer = find_min_path(graph, robot1, robot2)
print(answer)