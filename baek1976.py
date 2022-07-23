import sys
sys.stdin = open("baek1976.txt")


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


def is_linked(start, end, n):

    visited = [False] * (n+1)
    que = Queue(n*n)
    visited[start] = True
    que.enqueue(start)

    while not que.is_empty():
        node = que.dequeue()

        for next_node in graph[node]:
            if visited[next_node]:
                continue
            if next_node == end:
                return True
            visited[next_node] = True
            que.enqueue(next_node)
    return False


N = int(input())
M = int(input())

# 인접행렬 리스트로 해도 상관 없다 (최대 200 * 200 이니까)
graph = [[] for _ in range(0, N+1)]
temp = [0] * N
for i in range(0, N):
    temp[i] = list(map(int, input().split()))
travel = list(map(int, input().split()))

# 1번부터 N번까지 탐색할 수 있게 가공
for i in range(0, N):
    for j in range(0, N):
        if temp[i][j]:
            graph[i+1].append(j+1)
flag = True
for i in range(0, M-1):
    f = travel[i]
    t = travel[i+1]
    # f - t가 같은경우도 있다.. (이런걸 혼자 찾을 수 있어야 함)
    if (f != t) and (not is_linked(f, t, N)):
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")