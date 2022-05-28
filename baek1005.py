import sys
sys.stdin = open("baek1005.txt")
"""
위상정렬 연습 문제!

위상정렬은 진입차수(in_degree)와 진출 차수(out_degree)를 통해 순서를 짜는것

진입차수 == 특정 노드로 들어오는 간선의 갯수
진출차수 == 특정 노드에서 나가는 간선의 갯수

진입차수가 0인 정점(시작점)을 우선 배치 한 후, 그 정점에서 나가는 간선들을 제거하는 형태로 진행

위상 정렬 step
input 과정에서 graph 리스트에 담으면서
a -> b 관계에서 b노드 쪽 in_degree 를 +1씩 시켜주면서 저장한다.

Step1. 
모든 노드를 체크하면서 in_degree == 0 인값들을 전부 저장
(해당 노드로 들어오는 간선이 전혀 없는 상태이므로, 시작점이 된다.)

Step2.
BFS 개념으로 진행을 하며, 특정 노드에서 갈 수 있는 모든 방향을 체크,
다른 노드로 갈때마다, (now_node -> next_node)
간선은 제거시킨다. (in_degree[next_node] -= 1)

Step3.
in_degree[next_node] == 0 이된다면.
그 노드를 que에 담는다.


이 작업을 que가 빌 때까지 계속 진행하는것이 위상정렬!

# 이부분이 추가된것! (다음 단계 건물을 지으려면, 그 건물에 진입하는 노드들이 모두 완료되어야 하는 조건이므로!)
이 문제에서는, 여기서 DP[next_node] = max(DP[next_node], DP[now_node] + costs[next_node]) 


"""

class Queue:

    def __init__(self, capacity):
        self.max = capacity
        self.que = [0] * self.max
        self.front = 0
        self.rear = 0
        self.data = 0

    def enqueue(self, x):
        if self.data >= self.max:
            raise IndexError
        self.que[self.rear] = x
        self.data += 1
        self.rear += 1
        if self.rear == self.max:
            self.rear == 0
        return x

    def dequeue(self):
        if self.data <= 0:
            raise IndexError
        now = self.que[self.front]
        self.data -= 1
        self.front += 1
        if self.rear == self.max:
            self.front = 0
        return now

    def is_empty(self):
        return self.data <= 0


# 위상정렬 로직을 익히자
def acm_craft(graph, costs, end, n, degree):
    DP = [0] * (n+1)
    que = Queue(n*n*100)

    for i in range(1, N+1):
        # step1. 진입차수가 0인애들을(이 노드로 들어오는 점이 아예 없는것이므로 시작점) 전부 que에 enqueue한다 
        if degree[i] == 0:
            que.enqueue(i)
            # 1차이
            DP[i] += costs[i-1]

    while not que.is_empty():
        node = que.dequeue()

        for next_node in graph[node]:
            # 특정 노드로 진입될때마자 진입차수 -1 (제거시키는것)
            degree[next_node] -= 1
            # 해당 노드에 진입하는 노드들이 전부 완료되어야하므로, 현재 저장값보다 큰 상태가 확인되면 갱신
            DP[next_node] = max(DP[next_node], DP[node] + costs[next_node-1])

            # 진입차수 0이되면 (해당 노드에 들어오는 간선들이 전부 제거 된 상태) que에 enqueue
            if degree[next_node] == 0:
                que.enqueue(next_node)
    return DP[end]


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 코스트는 인덱스로 탐색 따라서 1차이남 조심!
    C = list(map(int, input().split()))
    # 진입 차수
    in_degree = [0] * (N+1)

    G = [[] for _ in range(0, N+1)]
    for i in range(0, K):
        # 건설 순서이므로, 단방향 그래프인것
        # 근데 나는 거꾸로 역방향 탐색하기로 했으므로 아래와같이 저장
        a, b = map(int, input().split())
        G[a].append(b)
        # b로 들어오는 간선의 갯수가 진입차수, 따라서 1씩 증가시킴
        in_degree[b] += 1

    W = int(input())
    answer = acm_craft(G, C, W, N, in_degree)
    print(answer)