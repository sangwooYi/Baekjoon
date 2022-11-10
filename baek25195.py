import sys
sys.stdin = open("baek25195.txt")


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


def is_possible(graph, arr):
    n = len(graph)

    gom_pos = {}
    for i in range(0, len(arr)):
        gom_pos[arr[i]] = 1
    
    que = Queue(n*100)
    if 1 in gom_pos.keys():
        return False
    que.enqueue(1)
    while not que.is_empty():
        node = que.dequeue()

        if len(graph[node]) == 0:
            return True
        for next_node in graph[node]:
            if next_node in gom_pos.keys():
                continue
            que.enqueue(next_node)
    return False

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(0, N+1)]
for i in range(0, M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
S = int(sys.stdin.readline())
goms = list(map(int, sys.stdin.readline().split()))

result = is_possible(graph, goms)

if result:
    print("yes")
else:
    print("Yes")