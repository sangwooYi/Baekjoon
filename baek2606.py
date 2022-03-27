import sys
sys.stdin = open("baek2606.txt")

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


def count_virus(arr, n):
    que = Queue(2*n)
    visited = [False] * (n+1)
    count = 0
    que.enqueue(1)
    visited[1] = True
    while not que.is_empty():
        now_node = que.dequeue()
        for next_node in arr[now_node]:
            if visited[next_node]:
                continue
            visited[next_node] = True
            count += 1
            que.enqueue(next_node)
    return count


N = int(input())
M = int(input())
# find union 으로 안풀리니까 그냥 BFS 진행
graph = [[] for _ in range(0, N+1)]
for i in range(0, M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
ans = count_virus(graph, N)
print(ans)