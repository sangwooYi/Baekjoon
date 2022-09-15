import sys
sys.stdin = open("baek14567.txt")

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


def pre_requiste():
    INF = 987654321
    res = [INF] * (N+1)
    que = Queue(50*N)

    for i in range(1, N+1):
        if in_degree[i] == 0:
            res[i] = 1
            que.enqueue((i, 1))
    
    while not que.is_empty():
        node, path = que.dequeue()

        for next_node in graph[node]:
            in_degree[next_node] -= 1

            if in_degree[next_node] == 0:
                res[next_node] = min(res[next_node], path+1)
                que.enqueue((next_node, path+1))

    return res[1:]

N, M = map(int, sys.stdin.readline().split())
in_degree = [0] * (N+1) 
graph = [[] for _ in range(0, N+1)]

for i in range(0, M):
    a, b = map(int, sys.stdin.readline().split())
    in_degree[b] += 1
    graph[a].append(b)

answer = pre_requiste()
print(" ".join(map(str, answer)))