import sys
sys.stdin = open("baek16940.txt")


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
    
    def peek(self):
        if self.data <= 0:
            raise IndexError
        return self.que[self.front]
    
    def is_empty(self):
        return self.data <= 0


N = int(sys.stdin.readline())
graph = [[] for _ in range(0, N+1)]

for i in range(0, N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

nodes = list(map(int, sys.stdin.readline().split()))

visited = [False] * (N+1)

que = Queue(5*N)
visited[1] = True
que.enqueue(1)



nodes.pop(0)
flag = True
cnt = 0
while not que.is_empty():
    now = que.dequeue()

    temp = []
    for next_node in graph[now]:
        if not visited[next_node]:
            visited[next_node] = True
            temp.append(next_node)

    while nodes:
        frn = nodes[0]
        if frn in temp:
            node = nodes[0]
            nodes.pop(0)
            cnt += 1
            que.enqueue(node)
        else:
            break

if cnt == N-1:
    print(1)
else:
    print(0)