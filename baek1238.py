import sys
sys.stdin = open("baek1238.txt")

"""
단방향이다!
idea.  (출발 => 도착 최단거리) + (도착 => 출발 최단거리) 의 합을 각각 계산 
노드가 1000개라 가능할지도?
기본적으로 다익스트라를 사용한다.

각 노드 - 도착점은 최단거리이나, 그 거리중 최댓값을 산출하면 됨
"""

class Queue:
    
    def __init__(self, capacity):
        self.max = capacity
        self.que = [0] * self.max
        self.data = 0
        self.front = 0
        self.rear = 0

    def enqueue(self, x):
        if self.data >= self.max:
            raise IndexError
        self.que[self.rear] = x
        self.data += 1
        self.rear += 1
        if self.rear == self.max:
            self.rear = 0
        return x
    
    def dequeue(self):
        if self.data <= 0:
            raise IndexError
        now = self.que[self.front]
        self.data -= 1
        self.front += 1
        if self.front == self.max:
            self.front = 0
        return now

    def is_empty(self):
        return self.data <= 0


def calc_path(graph, start, end, n):
    if start == end:
        return 0
    que = Queue(10000)
    INF = 987654321
    DP = [INF] * (n+1)
    DP[start] = 0
    que.enqueue((start, 0))

    while not que.is_empty():
        now = que.dequeue()
        node = now[0]
        cost = now[1]

        for next_node, next_cost in graph[node]:
            if DP[next_node] < cost + next_cost:
                continue
            DP[next_node] = cost + next_cost
            que.enqueue((next_node, DP[next_node]))
    return DP[end]

# 노드 갯수, 간선 갯수, 도착지 노드
N, M, X = map(int, input().split())
G = [[] for _ in range(0, N+1)]
for i in range(0, M):
    a, b, cost = map(int, input().split())
    G[a].append((b, cost))

answer = 0
for i in range(1, N+1):
    temp = calc_path(G, i, X, N) + calc_path(G, X, i, N)
    if answer < temp:
        answer = temp
print(answer)