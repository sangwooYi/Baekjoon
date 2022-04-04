import sys
sys.stdin = open("baek11403.txt")

"""
기본적으로 단방향 그래프!
1 ~ N 노드까지 순회하며,
각 노드마다 별개로 BFS 진행!
도착하는 노드를 체크해서 리스트를 만든다.
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


def find_path(start, graph, n):
    que = Queue(n * n)
    # 얘를 아예 return 해버린다.
    visited = [0] * n
    # start가 들를수 있는 애들을 전부 탐색
    for node in graph[start]:
        visited[node] = 1
        que.enqueue(node)
    
    while not que.is_empty():
        now = que.dequeue()
        for next_node in graph[now]:
            if visited[next_node]:
                continue
            visited[next_node] = 1
            que.enqueue(next_node)
    return visited



# 그냥 0 ~ N-1로가는게 더 편할듯
N = int(input())
MAP = [0] * N
for i in range(0, N):
    temp = list(map(int, input().split()))
    MAP[i] = temp
G = [[] for _ in range(0, N)]
for row in range(0, N):
    for col in range(0, N):
        if MAP[row][col]:
            G[row].append(col)

answer = [0] * N
for i in range(0, N):
    temp = find_path(i, G, N)
    answer[i] = temp
for row in range(0, N):
    for col in range(0, N):
        if col == N-1:
            print(answer[row][col], end="")
        else:
            print(answer[row][col], end=" ")
    if row < N-1:
        print()