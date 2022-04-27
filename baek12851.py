import sys
sys.stdin = open("baek12851.txt")
"""
BFS로 푼다!

BFS의 경우는 가장 빨리 도착한 애가 무조건 최소거리!
다익스트라랑 구분하자!
다익스트라는 가중치가 있기때문에,
먼저 도착해도, 나중에 도착한애보다 cost가 클 수 도있다!
다익스트라는 따라서 BFS 종료 이후에 DP체크!
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


def min_path(n, k):
    que = Queue(500000)
    INF = 98765
    DP = [INF] * 100001
    
    DP[n] = 0
    # BFS니까 k번 노드에 도착한 순서가 가장 빠른것
    # 근데 그와 동일한 횟수가 존재하면 count
    que.enqueue((n, 0))
    count = 0
    while not que.is_empty():
        node, path = que.dequeue()
        for i in range(0, 3):
            if i == 0:
                next_node = node - 1
                if next_node < 0:
                    continue
            elif i== 1:
                next_node = node + 1
                if next_node > 100000:
                    continue
            elif i == 2:
                next_node = node * 2
                if next_node > 100000:
                    continue
            if DP[next_node] < path+1:
                continue
            DP[next_node] = path+1
            if next_node == k:
                count += 1
            que.enqueue((next_node, path+1))
    print(DP[k])
    print(count)

N, K = map(int, input().split())
# K가 더 작은위치면 무조건 거꾸로가는거밖엔 없다.
if K <= N:
    print(N-K)
    print(1)
else:
    min_path(N, K)