import sys
sys.stdin = open("baek11724.txt")

"""
주어진 그래프가
단방향인지, 양방향인지(방향X) 반드시 확인!
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


def find_component(graph, n):
    que = Queue(n*n)

    visited = [False] * (n+1)
    count = 0
    
    while True:
        while not que.is_empty():
            node = que.dequeue()
            for next_node in graph[node]:
                if visited[next_node]:
                    continue
                visited[next_node] = True
                que.enqueue(next_node)
        flag = True
        for i in range(1, n+1):
            if not visited[i]:
                que.enqueue(i)
                visited[i] = True
                count += 1
                flag = False
                break
        if flag:
            return count



N, M = map(int, input().split())
G = [[] for _ in range(0, N+1)]
if M != 0:
    for i in range(0, M):
        a, b = map(int, sys.stdin.readline().split())
        G[a].append(b)
        G[b].append(a)
ans = find_component(G, N)
print(ans)